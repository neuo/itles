// Oxford 美音音标 → espeak-ng 的音素写法（en-us）。
// 输入约定：音节之间用 "." 隔开；主重音 ˈ、次重音 ˌ 写在音节开头。
//   例：fə.ˈtɑː.ɡrə.fi
// stress 参数（从 1 数）可以把主重音强行挪到第 k 个音节，用来放「重音读错是什么样」。

const TOKENS = [
  // 元音 + r（长的先匹配）
  ['aɪər', 'aI3'], ['aʊər', 'aU3'],
  ['ɑːr', 'A@'], ['ɔːr', 'o@'], ['ɜːr', '3:'],
  ['ɪr', 'i@3'], ['er', 'e@'], ['ʊr', 'U@'], ['ər', '3'],
  // 双元音
  ['eɪ', 'eI'], ['aɪ', 'aI'], ['ɔɪ', 'OI'], ['aʊ', 'aU'], ['əʊ', 'oU'], ['oʊ', 'oU'],
  // 长元音
  ['iː', 'i:'], ['uː', 'u:'], ['ɑː', 'A:'], ['ɔː', 'O:'], ['ɜː', '3:'],
  // 短元音
  ['ɪ', 'I'], ['e', 'E'], ['æ', 'a'], ['ʌ', 'V'], ['ʊ', 'U'], ['ə', '@'], ['i', 'i'], ['u', 'u:'],
  // 辅音
  ['tʃ', 'tS'], ['dʒ', 'dZ'],
  ['ʃ', 'S'], ['ʒ', 'Z'], ['θ', 'T'], ['ð', 'D'], ['ŋ', 'N'], ['ɡ', 'g'], ['g', 'g'],
  ['p', 'p'], ['b', 'b'], ['t', 't'], ['d', 'd'], ['k', 'k'], ['f', 'f'], ['v', 'v'],
  ['s', 's'], ['z', 'z'], ['m', 'm'], ['n', 'n'], ['l', 'l'], ['r', 'r'], ['w', 'w'],
  ['h', 'h'], ['j', 'j'],
];
const VOWEL_OUT = new Set(['aI3', 'aU3', 'A@', 'o@', '3:', 'i@3', 'e@', 'U@', '3',
  'eI', 'aI', 'OI', 'aU', 'oU', 'i:', 'u:', 'A:', 'O:', 'I', 'E', 'a', 'V', 'U', '@', 'i']);

const ALLOWED = /^[a-zæɑɔəɜɪʊʌʃʒθðŋɡːˈˌ.\s]+$/;

function tokenize(syl) {
  const out = [];
  let i = 0;
  while (i < syl.length) {
    const hit = TOKENS.find(([ipa]) => syl.startsWith(ipa, i));
    if (!hit) throw new Error('不认识的音标符号: ' + syl[i]);
    out.push(hit[1]);
    i += hit[0].length;
  }
  return out;
}

function splitSyllables(ipa) {
  return ipa.replace(/[\/\[\]]/g, '').trim().split(/[.\s]+/).filter(Boolean).map((raw) => {
    let mark = '';
    let body = raw;
    if (body.startsWith('ˈ')) { mark = "'"; body = body.slice(1); }
    else if (body.startsWith('ˌ')) { mark = ','; body = body.slice(1); }
    return { mark, body };
  });
}

function toEspeak(ipa, stress) {
  if (!ALLOWED.test(ipa.replace(/[\/\[\]]/g, ''))) throw new Error('音标里有不支持的字符');
  const syls = splitSyllables(ipa);
  if (stress) {
    if (stress < 1 || stress > syls.length) throw new Error('重音位置超出音节数');
    syls.forEach((s, idx) => {
      if (s.mark === "'") s.mark = '';
      if (idx === stress - 1) s.mark = "'";
    });
  }
  return syls.map(({ mark, body }) => {
    const toks = tokenize(body);
    let v = toks.findIndex((t) => VOWEL_OUT.has(t));
    if (v === -1) {
      // 没有元音的音节：成音节的 l / n / m（table 的 bl、nation 的 ʃn）
      const last = toks.length - 1;
      toks.splice(last, 1, '@', toks[last] === 'l' ? 'L' : toks[last]);
      v = last;
    }
    if (mark) toks.splice(v, 0, mark);
    return toks.join('');
  }).join('');
}

function syllableCount(ipa) {
  return splitSyllables(ipa).length;
}

// 主重音落在第几个音节（从 1 数）。没标重音：单音节算 1，多音节算 0。
function stressIndex(ipa) {
  const syls = splitSyllables(ipa);
  const i = syls.findIndex((s) => s.mark === "'");
  return i >= 0 ? i + 1 : (syls.length === 1 ? 1 : 0);
}

module.exports = { toEspeak, syllableCount, stressIndex, ALLOWED };
