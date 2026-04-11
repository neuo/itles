# IELTS Vocabulary Practice Tool

A local Node.js web application for IELTS vocabulary practice with spelling dictation and synonym association modes.

## Quick Start

```bash
cd /sessions/exciting-stoic-feynman/mnt/ielts/practice-app
./start.sh
```

Then open http://localhost:3456 in your browser.

## Features

### 1. 拼写听写 (Spelling Dictation)
- **智能随机**: Picks words weighted by error history (more errors = higher chance to appear)
- **错词重练**: Only practices words you've gotten wrong before
- **Category Selection**: Practice specific vocabulary categories
- **Auto-play TTS**: English (en-GB) pronunciation with 3 speed options (1x, 0.75x, 0.5x)
- **Immediate Feedback**: Shows correct answer, your answer, and pronunciation hints
- **Auto-save**: Results saved after each answer

### 2. 同义词联想 (Synonym Association)

#### 翻卡模式 (Flip Card Mode)
- Flip cards to reveal synonyms
- Rate each group: 认识 (know), 模糊 (fuzzy), 不认识 (don't know)
- Focus review on weak groups

#### 配对模式 (Match Mode)
- 60-second timer
- Match 5 words to their synonyms
- Visual feedback on correct matches

#### 联想模式 (Brainstorm Mode)
- 30-second countdown
- Type as many synonyms as you can think of
- Accepts partial matches

### 3. 统计 (Statistics)
- Total words practiced
- Overall accuracy percentage
- Top 15 most-missed words with attempt count
- Weakest synonym groups
- Export all data as Markdown

## Architecture

```
practice-app/
├── server.js          # Express-free Node.js HTTP server (built-in modules only)
├── data/
│   ├── words.json     # 500+ IELTS vocabulary words (16 categories)
│   ├── synonyms.json  # 40+ synonym groups
│   └── history.json   # Auto-created on first run
├── public/
│   └── index.html     # Single-page app (all CSS & JS embedded)
├── package.json       # No dependencies needed
└── start.sh          # Quick start script
```

## Data Persistence

All practice data is automatically saved to `data/history.json`:

```json
{
  "spelling": {
    "sessions": [
      {
        "date": "2026-04-06T15:30:00",
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
    "sessions": [...],
    "groupRatings": {
      "increase": {
        "rating": "模糊",
        "lastSeen": "2026-04-06"
      }
    }
  }
}
```

## API Endpoints

- `GET /` - Serve the single-page app
- `GET /api/words` - Get all vocabulary words by category
- `GET /api/synonyms` - Get all synonym groups
- `GET /api/history` - Get practice history
- `POST /api/history` - Save/update practice history
- `GET /api/stats` - Get computed statistics

## Vocabulary Categories

1. 今日错词 (Today's Errors) - 6 words
2. 住宿/租房 (Housing) - 35 words
3. 旅行/交通 (Travel/Transport) - 29 words
4. 银行/金融 (Banking/Finance) - 15 words
5. 学术/课程 (Academic) - 24 words
6. 职业/工作 (Career) - 18 words
7. 运动/健身 (Sports/Fitness) - 16 words
8. 餐饮 (Dining) - 12 words
9. 娱乐 (Entertainment) - 11 words
10. 地图题方位词 (Map Directions) - 15 words
11. 医疗/健康 (Medical/Health) - 15 words
12. 环境/自然 (Environment/Nature) - 12 words
13. 时间/日期 (Time/Date) - 13 words
14. 易错重灾区 (Common Mistakes) - 25 words

Plus 40+ synonym groups covering essential IELTS writing and speaking vocabulary.

## Technology Stack

- **Server**: Node.js (built-in http, fs, path modules only)
- **Frontend**: HTML5, CSS3 (Apple design system), Vanilla JavaScript
- **Audio**: Web Speech Synthesis API
- **Data**: JSON files (no database needed)
- **No dependencies**: `npm install` not required

## Notes

- The app uses browser localStorage to track UI state (tab selection, etc.)
- All data persists to `data/history.json` via POST requests
- History is auto-merged on each save (new data supplements old data)
- Speech synthesis requires browser support (Chrome, Safari, Edge)
