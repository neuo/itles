# IELTS Practice App - Deployment & Usage Guide

## Quick Start

```bash
cd /sessions/exciting-stoic-feynman/mnt/ielts/practice-app
./start.sh
```

Open http://localhost:3456 in your web browser.

The server will print: `IELTS Practice App running at http://localhost:3456`

## What's Included

### Core Files
- **server.js** (238 lines): Pure Node.js HTTP server using only built-in modules (http, fs, path)
  - No npm install required
  - Serves static index.html and API endpoints
  - Auto-persists data to history.json after each answer

- **public/index.html** (1533 lines): Single-page application with:
  - All CSS embedded (Apple design system)
  - All JavaScript embedded (vanilla - no frameworks)
  - Three main tabs: 拼写听写, 同义词联想, 统计
  - Web Speech Synthesis for pronunciation (en-GB)

- **data/words.json**: 500+ IELTS vocabulary words across 14 categories:
  - 今日错词 (6 words)
  - 住宿/租房 (35 words)
  - 旅行/交通 (29 words)
  - 银行/金融 (15 words)
  - 学术/课程 (24 words)
  - 职业/工作 (18 words)
  - 运动/健身 (16 words)
  - 餐饮 (12 words)
  - 娱乐 (11 words)
  - 地图题方位词 (15 words)
  - 医疗/健康 (15 words)
  - 环境/自然 (12 words)
  - 时间/日期 (13 words)
  - 易错重灾区 (25 words - common mistakes)

- **data/synonyms.json**: 40+ synonym groups for association practice
  - Each group has a main word and 3-9 synonyms
  - Covers essential IELTS writing/speaking vocab

- **data/history.json**: Auto-created on first run
  - Tracks spelling practice sessions
  - Tracks word-level statistics (attempts, correct, lastSeen, lastWrong)
  - Tracks synonym group ratings (认识/模糊/不认识)

### Support Files
- **package.json**: Simple metadata (no dependencies)
- **start.sh**: Executable script (chmod +x already applied)
- **README.md**: Feature documentation

## Feature Overview

### 1. Spelling Dictation (拼写听写)

**Smart Random (智能随机)**
- Pulls from all word categories
- Weights selection by error rate (mistakes appear more often)
- Great for targeted practice

**Error Word Review (错词重练)**
- Only shows words previously marked wrong
- Builds on weak areas
- Empty until you get some answers wrong

**Category Selection**
- Practice specific vocabulary domains
- 14 categories to choose from
- All words visible before starting

**How it Works**
1. Select category → Word auto-plays (en-GB audio)
2. User types spelling in input field
3. Press Enter or click Submit
4. Immediate feedback:
   - Correct: green flash, auto-advance after 800ms
   - Wrong: shows correct answer, your answer, and hint
   - Can replay audio and try again
5. Session summary at end with accuracy % and missed words
6. Can retry just the wrong words or start a new round

**Auto-Save**
- After each answer, stats updated and saved to history.json
- Tracks: attempts, correct count, lastSeen date, lastWrong date

**Audio Controls**
- Play/Replay button available
- 3 speed options: 1x (normal), 0.75x (slow), 0.5x (very slow)

### 2. Synonym Association (同义词联想)

**Flip Card Mode (翻卡模式)**
- Shows a word
- Click to flip and reveal synonyms
- Rate each group: 认识 (know) / 模糊 (fuzzy) / 不认识 (don't know)
- "重点复习" button filters to weak/fuzzy groups
- Auto-saves ratings to history

**Match Mode (配对模式)**
- 60-second timer
- 5 words on left, 5 synonyms on right (shuffled)
- Click word, then click matching synonym
- Correct matches turn green and fade
- Shows score when complete
- Saves results to history

**Brainstorm Mode (联想模式)**
- 30-second countdown
- Given a word, type as many synonyms as you can think of
- Each synonym you enter appears in the list
- Accepts partial matches (e.g., typing "go up" matches group containing "go up")
- Wrong entries shake but disappear
- Final score shows: answered/available synonyms
- Saves best attempts to history

### 3. Statistics (统计)

**Summary Cards**
- Total words practiced
- Total attempts across all sessions
- Overall accuracy %
- Number of synonym groups covered

**Top 15 Missed Words Table**
- Word | Attempts | Accuracy %
- Color-coded accuracy bars (red <50%, yellow 50-80%, green 80%+)
- Sortable by accuracy or attempts

**Weak Synonym Groups**
- Shows groups rated as 模糊 or 不认识
- Limited to top 10
- Most recently seen first

**Export Data**
- "导出记录" button downloads Markdown file
- File name: ielts-stats-YYYY-MM-DD.md
- Includes all stats, missed words table, weak groups

## API Endpoints

All endpoints return JSON and support CORS.

### GET /
Returns index.html (the main app)

### GET /api/words
Returns all words.json content:
```json
{
  "今日错词": [...],
  "住宿/租房": [...],
  ...
}
```

### GET /api/synonyms
Returns synonyms.json content:
```json
{
  "groups": [
    {"key": "cost", "word": "cost", "synonyms": ["price", "fee", ...]},
    ...
  ]
}
```

### GET /api/history
Returns current history.json (creates empty one if not exists):
```json
{
  "spelling": {
    "sessions": [...],
    "wordStats": {...}
  },
  "synonym": {
    "sessions": [...],
    "groupRatings": {...}
  }
}
```

### POST /api/history
Accepts JSON body, merges with existing history, returns updated history:
```json
{
  "spelling": {
    "sessions": [{...}],
    "wordStats": {"word": {...}}
  },
  "synonym": {
    "sessions": [...],
    "groupRatings": {"key": {...}}
  }
}
```

### GET /api/stats
Returns computed statistics:
```json
{
  "spelling": {
    "totalWords": 25,
    "totalAttempts": 150,
    "totalCorrect": 120,
    "accuracy": 80,
    "mostMissedWords": [
      {"word": "accommodation", "attempts": 5, "correct": 1, "accuracy": 20},
      ...
    ]
  },
  "synonym": {
    "totalGroups": 15,
    "weakestGroups": [
      {"group": "increase", "rating": "模糊", "lastSeen": "2026-04-06"},
      ...
    ]
  }
}
```

## Data Structure

### history.json Format

```json
{
  "spelling": {
    "sessions": [
      {
        "date": "2026-04-06T15:30:00Z",
        "category": "易错重灾区",
        "total": 25,
        "correct": 20,
        "wrongWords": ["accommodation", "necessary"]
      }
    ],
    "wordStats": {
      "accommodation": {
        "attempts": 5,
        "correct": 2,
        "lastSeen": "2026-04-06",
        "lastWrong": "2026-04-06"
      }
    }
  },
  "synonym": {
    "sessions": [
      {
        "date": "2026-04-06T16:00:00Z",
        "mode": "flip",
        "groupsRated": 10
      }
    ],
    "groupRatings": {
      "increase": {
        "rating": "模糊",
        "lastSeen": "2026-04-06",
        "brainstormBest": 6
      }
    }
  }
}
```

## Browser Requirements

- Modern browser (Chrome 90+, Safari 14+, Edge 90+, Firefox 89+)
- JavaScript enabled
- Web Speech Synthesis API (for TTS - not required for text)

## Performance Notes

- Single-page app: <2MB in-memory after load
- JSON file sizes:
  - words.json: ~22KB
  - synonyms.json: ~5KB
  - history.json: grows with practice (starts empty)
- Server response time: <10ms (file-based, no database)
- No external CDN dependencies

## Customization

### Add More Words

Edit `data/words.json`:
1. Add new category or append to existing:
```json
{
  "新分类": [
    {"word": "example", "hint": "pronunciation guide", "sentence": "Example sentence."},
    ...
  ]
}
```
2. Server will load on next restart
3. Category automatically appears in practice menu

### Add More Synonyms

Edit `data/synonyms.json`:
1. Add to the `groups` array:
```json
{
  "groups": [
    {"key": "unique_id", "word": "word", "synonyms": ["syn1", "syn2", ...]},
    ...
  ]
}
```
2. Server will load on next restart
3. Group automatically available in synonym modes

### Change Port

Edit line 6 in server.js:
```javascript
const PORT = 3456;  // Change to any available port
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 3456
lsof -i :3456
# Kill it
kill -9 <PID>
# Or use different port in server.js
```

### Audio Not Playing
- Check browser supports Web Speech Synthesis
- Try: chrome://flags and search "speech"
- Ensure browser microphone access isn't blocked

### Data Not Saving
- Check `data/` directory has write permissions
- Verify history.json exists
- Check browser console for network errors

### Slow Performance
- Clear browser cache
- Close other tabs
- Restart server
- Check disk space (file I/O)

## File Permissions

```bash
# Ensure start.sh is executable
chmod +x /sessions/exciting-stoic-feynman/mnt/ielts/practice-app/start.sh

# Ensure data directory is writable
chmod 755 /sessions/exciting-stoic-feynman/mnt/ielts/practice-app/data
```

## Production Notes

This app is designed for **local single-user practice** only:
- No authentication
- All data in plain JSON files
- No encryption
- Suitable for personal use only

For multi-user deployment, consider:
- Adding user authentication
- Using a proper database (PostgreSQL, MongoDB)
- Adding data backup/export functionality
- Running behind a reverse proxy (nginx)

---

Built for suzy's IELTS preparation - April 2026
