#!/bin/sh
# 让练习网页在后台常驻（macOS launchd，只装在当前用户下）。
#   登录后自动启动 · 进程挂了自动拉起 · 改了 server.js 或 lib/ 自动重启（node --watch）
#   public/ 里的页面文件和 data/ 里的数据每次请求都现读，改了不用重启。
#
#   phonics/app/service.sh install     装上并启动（重复跑 = 按当前路径重装）
#   phonics/app/service.sh restart     重启
#   phonics/app/service.sh status      在不在跑、网页通不通
#   phonics/app/service.sh log         最近的日志
#   phonics/app/service.sh uninstall   停掉并卸载
set -eu

LABEL=local.ielts.phonics
PORT=4310
APP="$(cd "$(dirname "$0")" && pwd)"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG="$HOME/Library/Logs/phonics-server.log"
DOMAIN="gui/$(id -u)"
URL="http://localhost:$PORT"

loaded() { launchctl print "$DOMAIN/$LABEL" >/dev/null 2>&1; }
http() { curl -s -o /dev/null -m 3 -w '%{http_code}' "$URL/api/overview" 2>/dev/null || true; }
# 等网页起来，最多 10 秒
wait_up() {
  i=0
  while [ $i -lt 20 ]; do
    [ "$(http)" = 200 ] && return 0
    sleep 0.5; i=$((i + 1))
  done
  return 1
}
report() {
  if ! loaded; then echo "没装。装上：phonics/app/service.sh install"; return 1; fi
  pid="$(launchctl print "$DOMAIN/$LABEL" | awk '/^[[:space:]]*pid = /{print $3; exit}')"
  code="$(http)"
  echo "launchd：已装（$LABEL）· 进程 ${pid:-没在跑}"
  echo "网页：$URL → ${code:-连不上}"
  [ "$code" = 200 ]
}

case "${1:-}" in
  install)
    NODE="$(command -v node)" || { echo "找不到 node"; exit 1; }
    BIN="$(dirname "$NODE")"
    ESPEAK="$(command -v espeak-ng || true)"
    [ -n "$ESPEAK" ] && BIN="$BIN:$(dirname "$ESPEAK")"
    mkdir -p "$(dirname "$PLIST")" "$(dirname "$LOG")"
    loaded && launchctl bootout "$DOMAIN/$LABEL" 2>/dev/null || true
    cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>$NODE</string>
    <string>--watch</string>
    <string>--watch-preserve-output</string>
    <string>$APP/server.js</string>
    <string>--port</string>
    <string>$PORT</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>$BIN:/usr/bin:/bin</string></dict>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ThrottleInterval</key><integer>5</integer>
  <key>StandardOutPath</key><string>$LOG</string>
  <key>StandardErrorPath</key><string>$LOG</string>
</dict>
</plist>
EOF
    # 刚 bootout 完马上 bootstrap 偶尔会撞上，等一下再试
    launchctl bootstrap "$DOMAIN" "$PLIST" 2>/dev/null || { sleep 1; launchctl bootstrap "$DOMAIN" "$PLIST"; }
    wait_up || { echo "装上了，但网页没起来。看日志：phonics/app/service.sh log"; report || true; exit 1; }
    report
    ;;
  restart)
    loaded || { echo "没装。装上：phonics/app/service.sh install"; exit 1; }
    launchctl kickstart -k "$DOMAIN/$LABEL"
    wait_up || { echo "重启了，但网页没起来。看日志：phonics/app/service.sh log"; report || true; exit 1; }
    report
    ;;
  status)
    report
    ;;
  log)
    tail -n "${2:-30}" "$LOG" 2>/dev/null || echo "还没有日志"
    ;;
  uninstall)
    loaded && launchctl bootout "$DOMAIN/$LABEL" || true
    rm -f "$PLIST"
    echo "已卸载。日志还留在 $LOG"
    ;;
  *)
    echo "用法：phonics/app/service.sh install | restart | status | log [行数] | uninstall"
    exit 1
    ;;
esac
