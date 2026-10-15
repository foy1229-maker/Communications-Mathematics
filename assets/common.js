/* 공통: 수식 렌더링과 풀이 기록(이 브라우저에만 저장) */
(function () {
  var KEY = 'cm2.progress.v1';
  var memory = {};

  function parse(raw) {
    try { return raw ? JSON.parse(raw) : null; } catch (e) { return null; }
  }

  /* 로그인 기능을 없애기 전에 쓰던 저장값 정리 — 한 번 옮기고 나면 더 할 일이 없어요.
     계정마다 따로 저장했던 기록(cm2.progress.v1:아이디)을 기록 하나로 합쳐요.
     이미 있는 기록 → 마지막으로 로그인했던 계정 → 나머지 계정 순서로, 아직 표시가 없는 문제만 채워요.
     다 옮긴 뒤에는 계정별 기록과 계정 · 로그인 상태 저장값을 지워요. */
  function lastAccount(s) {
    var found = [];
    try { found.push(s.getItem('cm2.session.v1')); } catch (e) { /* 무시 */ }
    try {
      var m = document.cookie.match(/(?:^|; )cm2_session=([^;]*)/);
      if (m) found.push(decodeURIComponent(m[1]));
    } catch (e) { /* 무시 */ }
    try { found.push(window.sessionStorage.getItem('cm2.session.v1')); } catch (e) { /* 무시 */ }
    for (var i = 0; i < found.length; i++) {
      var v = parse(found[i]);
      if (v && typeof v.id === 'string') return v.id;
    }
    return '';
  }

  function mergeOldAccounts() {
    var s;
    try { s = window.localStorage; } catch (e) { return; }
    if (!s) return;
    var prefix = KEY + ':';
    try {
      var keys = [];
      for (var i = 0; i < s.length; i++) {
        var k = s.key(i);
        if (k && k.indexOf(prefix) === 0) keys.push(k);
      }
      if (keys.length) {
        var last = prefix + lastAccount(s);
        keys.sort(function (a, b) { return (b === last) - (a === last); });
        var merged = parse(s.getItem(KEY)) || {};
        keys.forEach(function (key) {
          var old = parse(s.getItem(key)) || {};
          for (var id in old) {
            if (Object.prototype.hasOwnProperty.call(old, id) && !Object.prototype.hasOwnProperty.call(merged, id)) merged[id] = old[id];
          }
        });
        s.setItem(KEY, JSON.stringify(merged));   // 여기서 실패하면 계정별 기록을 지우지 않고 그대로 둬요
        keys.forEach(function (key) { s.removeItem(key); });
      }
      s.removeItem('cm2.accounts.v1');
      s.removeItem('cm2.session.v1');
    } catch (e) { return; }
    try { window.sessionStorage.removeItem('cm2.session.v1'); } catch (e) { /* 무시 */ }
    try {
      if (/(?:^|; )cm2_session=/.test(document.cookie)) {
        document.cookie = 'cm2_session=; Max-Age=0; SameSite=Lax' + (location.protocol === 'https:' ? '; Secure' : '');
      }
    } catch (e) { /* 무시 */ }
  }
  mergeOldAccounts();

  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) || {} : memory;
    } catch (e) {
      return memory;
    }
  }

  function save(progress) {
    memory = progress;
    try { window.localStorage.setItem(KEY, JSON.stringify(progress)); } catch (e) { /* 저장 불가: 메모리에만 유지 */ }
  }

  function renderMath(el) {
    if (!el || typeof window.renderMathInElement !== 'function') return;
    window.renderMathInElement(el, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false }
      ],
      throwOnError: false,
      strict: 'ignore'
    });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function bankUrl(p) {
    return 'bank.html?level=' + p.lv + '#p' + p.id;
  }

  window.CM = { load: load, save: save, renderMath: renderMath, escapeHtml: escapeHtml, bankUrl: bankUrl };
})();
