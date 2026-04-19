const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3456;
const DATA_DIR = path.join(__dirname, 'data');
const PUBLIC_DIR = path.join(__dirname, 'public');

// Ensure data directory exists
if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}

// Helper to read JSON file
function readJSON(filePath) {
  if (!fs.existsSync(filePath)) {
    return null;
  }
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

// Helper to write JSON file
function writeJSON(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

// Get or create history.json
function getHistory() {
  const historyPath = path.join(DATA_DIR, 'history.json');
  let history = readJSON(historyPath);

  if (!history) {
    history = {
      spelling: {
        sessions: [],
        wordStats: {},
        starredWords: {}
      },
      synonym: {
        sessions: [],
        groupRatings: {}
      },
      number: {
        sessions: [],
        sentenceStats: {}
      }
    };
    writeJSON(historyPath, history);
  }

  // Backfill number section for older history.json
  if (!history.number) {
    history.number = { sessions: [], sentenceStats: {} };
  }

  return history;
}

// Save history
function saveHistory(history) {
  const historyPath = path.join(DATA_DIR, 'history.json');
  writeJSON(historyPath, history);
}

// Merge incoming history data
function mergeHistory(incomingData) {
  const history = getHistory();

  if (incomingData.spelling) {
    if (incomingData.spelling.sessions) {
      history.spelling.sessions = incomingData.spelling.sessions;
    }
    if (incomingData.spelling.wordStats) {
      history.spelling.wordStats = {
        ...history.spelling.wordStats,
        ...incomingData.spelling.wordStats
      };
    }
    if (incomingData.spelling.starredWords) {
      history.spelling.starredWords = {
        ...history.spelling.starredWords,
        ...incomingData.spelling.starredWords
      };
    }
  }

  if (incomingData.synonym) {
    if (incomingData.synonym.sessions) {
      history.synonym.sessions = incomingData.synonym.sessions;
    }
    if (incomingData.synonym.groupRatings) {
      history.synonym.groupRatings = {
        ...history.synonym.groupRatings,
        ...incomingData.synonym.groupRatings
      };
    }
  }

  if (incomingData.number) {
    if (!history.number) history.number = { sessions: [], sentenceStats: {} };
    if (incomingData.number.sessions) {
      history.number.sessions = incomingData.number.sessions;
    }
    if (incomingData.number.sentenceStats) {
      history.number.sentenceStats = {
        ...history.number.sentenceStats,
        ...incomingData.number.sentenceStats
      };
    }
  }

  saveHistory(history);
  return history;
}

// Calculate stats
function calculateStats() {
  const history = getHistory();

  // Spelling stats
  let totalAttempts = 0;
  let totalCorrect = 0;
  const wordStats = history.spelling.wordStats;

  for (const word in wordStats) {
    const stat = wordStats[word];
    totalAttempts += stat.attempts || 0;
    totalCorrect += stat.correct || 0;
  }

  const accuracy = totalAttempts > 0 ? Math.round((totalCorrect / totalAttempts) * 100) : 0;

  // Most missed words
  const missedWords = Object.keys(wordStats)
    .map(word => ({
      word,
      attempts: wordStats[word].attempts || 0,
      correct: wordStats[word].correct || 0,
      accuracy: wordStats[word].attempts > 0
        ? Math.round((wordStats[word].correct / wordStats[word].attempts) * 100)
        : 0
    }))
    .sort((a, b) => a.accuracy - b.accuracy || b.attempts - a.attempts)
    .slice(0, 15);

  // Synonym weakest groups
  const groupRatings = history.synonym.groupRatings;
  const weakestGroups = Object.keys(groupRatings)
    .map(group => ({
      group,
      rating: groupRatings[group].rating || '未开始',
      lastSeen: groupRatings[group].lastSeen
    }))
    .filter(g => g.rating === '不认识' || g.rating === '模糊')
    .sort((a, b) => new Date(b.lastSeen) - new Date(a.lastSeen))
    .slice(0, 15);

  return {
    spelling: {
      totalWords: Object.keys(wordStats).length,
      totalAttempts,
      totalCorrect,
      accuracy,
      mostMissedWords: missedWords
    },
    synonym: {
      totalGroups: Object.keys(groupRatings).length,
      weakestGroups
    }
  };
}

// Request handler
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;
  const method = req.method;

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  // Static files
  if (pathname === '/' && method === 'GET') {
    const indexPath = path.join(PUBLIC_DIR, 'index.html');
    fs.readFile(indexPath, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
        return;
      }
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(data);
    });
    return;
  }

  // API: GET /api/words
  if (pathname === '/api/words' && method === 'GET') {
    const wordsPath = path.join(DATA_DIR, 'words.json');
    const words = readJSON(wordsPath);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(words || {}));
    return;
  }

  // API: GET /api/synonyms
  if (pathname === '/api/synonyms' && method === 'GET') {
    const synonymsPath = path.join(DATA_DIR, 'synonyms.json');
    const synonyms = readJSON(synonymsPath);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(synonyms || { groups: [] }));
    return;
  }

  // API: GET /api/numbers
  if (pathname === '/api/numbers' && method === 'GET') {
    const numbersPath = path.join(DATA_DIR, 'numbers.json');
    const numbers = readJSON(numbersPath);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(numbers || { sentences: [] }));
    return;
  }

  // API: GET /api/history
  if (pathname === '/api/history' && method === 'GET') {
    const history = getHistory();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(history));
    return;
  }

  // API: POST /api/history
  if (pathname === '/api/history' && method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const incomingData = JSON.parse(body);
        const updatedHistory = mergeHistory(incomingData);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(updatedHistory));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
      }
    });
    return;
  }

  // API: GET /api/stats
  if (pathname === '/api/stats' && method === 'GET') {
    const stats = calculateStats();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(stats));
    return;
  }

  // 404
  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('404 Not Found');
});

server.listen(PORT, () => {
  console.log(`IELTS Practice App running at http://localhost:${PORT}`);
});
