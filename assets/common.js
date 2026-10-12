/* 공통: 수식 렌더링과 풀이 기록(이 브라우저에만 저장) */
(function () {
  var KEY = 'cm2.progress.v1';
  var memory = {};

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
