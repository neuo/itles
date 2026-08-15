#!/usr/bin/env bash
# writing-drill 口径一致性检查（§0.0 编辑闸第 ③ 条的执行体）
#
# 为什么存在（八审）：
#   §0.0 管的是【改这份 spec 本身】，而那发生在审查/维护时，不在 session 里。
#   G6 断言 11 只在 session 收尾跑，且 SKILL.md 根本不在它的输入里 ——
#   证据：断言 11 装上去之后，`【G-R3 对账闸】| 同【G6 对账闸】(12 条…)` 就在它三行之外活了下来。
#   ⇒ 改完 spec 就跑一次这个脚本。它只做一件事：把【应当全库一致的口径】数一遍，不一致就喊。
#
# 用法：bash .claude/skills/writing-drill/check.sh
# 退出码：0 = 全过 · 1 = 有不一致
#
# ⚠️ 本脚本只【读和数】，绝不写任何内容文件 —— 内容一律手工 Edit（她 08-04 的禁令）。

set -u
cd "$(dirname "$0")/../../.." || exit 2

SKILL=.claude/skills/writing-drill/SKILL.md
SCORING=.claude/skills/writing-drill/scoring.md
PROFILE=writing-band7/drill/profile.md
LOG=writing-band7/drill/log.md
BANK=writing-band7/drill/bank.md
FILES="$SKILL $SCORING $PROFILE $LOG $BANK"   # 九审补 bank.md：它是五份真源之一，🎯 行规则和代号范围都在里面

fail=0
bad() { printf '❌ %s\n' "$*"; fail=1; }
ok()  { printf '✅ %s\n' "$*"; }

echo "=== writing-drill 口径检查 ==="

# ── ① 行数：§0.1 表声明值 vs 真实 wc -l（F106 已复发五次）──────────────
echo
echo "-- ① SKILL.md 行数 --"
real=$(wc -l < "$SKILL" | tr -d ' ')
declared=$(grep -m1 '本文件行数 = ' "$SKILL" | grep -oE '[0-9]+' | head -1)
if [ "$real" = "$declared" ]; then
  ok "$real 行，与 §0.1 一致"
else
  bad "wc -l = $real ，§0.1 写着 $declared —— 三个数（行数/学习日合计/百分比）都要重算"
fi

# ── ② 工具脚本：SKILL 里点名的三个脚本必须存在且能跑（v2 起，替代原 G6 断言条数）──
echo
echo "-- ② 工具脚本 --"
tool_bad=0
for t in writing-band7/drill/snapshot.py writing-band7/drill/queue.py writing-band7/drill/pick_question.py; do
  if [ ! -f "$t" ]; then bad "SKILL 点名的 $t 不存在"; tool_bad=1
  elif ! python3 -c "compile(open('$t',encoding='utf-8').read(),'$t','exec')" 2>/dev/null; then
    bad "$t 语法错，跑不起来"; tool_bad=1
  fi
done
# SKILL 里提到的脚本路径必须都在上面这份名单里（防写了个不存在的工具）
for t in $(grep -oE 'writing-band7/drill/[a-z_]+\.py' "$SKILL" | sort -u); do
  [ -f "$t" ] || { bad "SKILL 引用了不存在的脚本 $t"; tool_bad=1; }
done
[ $tool_bad -eq 0 ] && ok "三个工具脚本齐全且可编译"

# ── ③ 模式计数器行数：profile §5 实际行 vs 全库"N 行"的说法 ────────────
echo
echo "-- ③ 模式计数器行数 --"
rows=$(sed -n '/每篇必须把下面/,/^---$/p' "$PROFILE" | grep -cE '^\| \*{0,2}(P|W)[0-9]+')
echo "   profile §5 实际模式行 = ${rows}"
counter_decls=$(grep -ohE '[0-9]+ 行模式计数器|[0-9]+ 行计数器|[0-9]+ 行里的|[0-9]+ 行全动|[0-9]+ 行【全部】|[0-9]+ 次判断|[0-9]+ 行是不是都动过|这 [0-9]+ 行同时' $FILES \
                | grep -oE '[0-9]+' | sort -u)
for n in ${counter_decls}; do
  [ "${n}" = "${rows}" ] || bad "有一处写着 ${n} 行/次，实际 ${rows} 行"
done
[ "${counter_decls}" = "${rows}" ] && ok "各处一致（${rows} 行）"

# ── ④ 代号范围：P1-P<n> vs profile §1 实际定义到 P 几 ───────────────────
echo
echo "-- ④ 代号范围 --"
maxp=$(grep -oE '^### P[0-9]+' "$PROFILE" | grep -oE '[0-9]+' | sort -n | tail -1)
echo "   profile §1 定义到 P${maxp}"
range_decls=$(grep -vE "原来|原写" $FILES 2>/dev/null | grep -ohE "P1[–-]P[0-9]+" | grep -oE '[0-9]+$' | sort -u)
for n in ${range_decls}; do
  if [ "${n}" != "${maxp}" ]; then
    bad "有一处写着 P1-P${n}，实际定义到 P${maxp}"
    grep -rnE "P1[–-]P${n}([^0-9]|\$)" $FILES | sed 's/^/      /'
  fi
done
[ "${range_decls}" = "${maxp}" ] && ok "各处一致（P1-P${maxp}）"

# ── ⑤ 死指针：引用了 scoring.md 里不存在的小节 ─────────────────────────
echo
echo "-- ⑤ 死指针 --"
dead_ptr=0
for sec in $(grep -ohE '`?scoring(\.md)?`? ?§[0-9]+(\.[0-9]+[a-z]?)?' $FILES \
             | sed 's/.*§//' | sort -u); do
  grep -qE "^#{2,4} ${sec}[ .·]" "$SCORING" || { bad "scoring.md 里没有 §${sec}"; dead_ptr=1; }
done
[ $dead_ptr -eq 0 ] && ok "所有 scoring.md 小节引用都存在"

# ── ⑥ 已废弃的口径不该复活（教训记录里出现是允许的）─────────────────────
echo
echo "-- ⑥ 已废弃口径 --"
revived=0
for dead in 发散告警 抽查槽位 P_K 靶子外复发; do
  hits=$(grep -rn -- "$dead" $FILES 2>/dev/null \
         | grep -vE "删|废|原来|原写|更正|审|F[0-9]+|教训|修订史|不再统计|一并|改名|→|取代|换成|二修|三修|四修|不同的量|:[0-9]+:>" \
         | wc -l | tr -d ' ')
  if [ "$hits" != "0" ]; then
    bad "已废除的「${dead}」有 ${hits} 处不在教训记录里"
    grep -rn -- "$dead" $FILES 2>/dev/null \
      | grep -vE "删|废|原来|原写|更正|审|F[0-9]+|教训|修订史|不再统计|一并|改名|→|取代|换成|二修|三修|四修|不同的量|:[0-9]+:>" | sed 's/^/      /'
    revived=1
  fi
done
[ $revived -eq 0 ] && ok "四个废弃口径都只活在教训记录里"

echo
if [ $fail -eq 0 ]; then
  echo "=== 全部通过 ==="
else
  echo "=== 有不一致，见上面的 ❌（一律手工 Edit 修，禁脚本改内容）==="
fi
exit $fail
