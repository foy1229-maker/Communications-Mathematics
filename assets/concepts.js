/* 개념 정리: 수식 렌더링, 유형별 연습 문제 연결, 목차 위치 표시 */
(function () {
  var D = window.CM_DATA;
  var progress = CM.load();

  /* 유형 → 문제 번호 링크 */
  if (D) {
    var types = document.querySelectorAll('.type[data-type]');
    for (var i = 0; i < types.length; i++) {
      var key = types[i].getAttribute('data-type');
      var list = D.problems.filter(function (p) { return p.type === key; });
      var box = types[i].querySelector('.practice');
      if (!box) continue;
      if (!list.length) { box.remove(); continue; }
      // 단계별로 묶어서: "1단계 3 · 2단계 2/4 …" → bank.html?level=N&type=유형 (맞은 수/문제 수)
      box.innerHTML = '<span>연습 ' + list.length + '문제</span>' + [1, 2, 3, 4].map(function (lv) {
        var items = list.filter(function (p) { return p.lv === lv; });
        if (!items.length) return '';
        var done = items.filter(function (p) { return progress[p.id] === 'ok'; }).length;
        return '<a href="bank.html?level=' + lv + '&amp;type=' + encodeURIComponent(key) + '"' +
          (done === items.length ? ' class="done"' : '') +
          ' title="' + lv + '단계에서 이 유형 ' + items.length + '문제만 보기' + (done ? ' (맞음 ' + done + ')' : '') + '">' +
          lv + '단계 ' + (done ? done + '/' : '') + items.length + '</a>';
      }).join('');
      // 유형 → 풀이 행동강령 카드 (assets/playbook-map.js)
      var pbMap = window.CM_PLAYBOOK && window.CM_PLAYBOOK.types;
      if (pbMap && pbMap[key]) {
        box.insertAdjacentHTML('beforeend', '<a class="pb-link" href="playbook.html#' + pbMap[key] + '" title="이 유형의 세부 행동강령·상황별 대처">행동강령 →</a>');
      }
    }
    var counts = { types: Object.keys(D.types).length, problems: D.problems.length };
    var cEls = document.querySelectorAll('[data-count]');
    for (var c = 0; c < cEls.length; c++) {
      var k = cEls[c].getAttribute('data-count');
      if (counts[k] != null) cEls[c].textContent = counts[k];
    }
  }

  CM.renderMath(document.querySelector('main'));
  CM.renderMath(document.querySelector('.hero'));

  /* 목차: 지금 보고 있는 단원 표시 */
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a[href^="#"]'));
  var targets = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
  if ('IntersectionObserver' in window) {
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var current = null;
      for (var t = 0; t < targets.length; t++) {
        if (targets[t] && visible[targets[t].id]) { current = targets[t].id; break; }
      }
      if (!current) return;
      links.forEach(function (a) {
        var on = a.getAttribute('href') === '#' + current;
        a.classList.toggle('on', on);
        if (on && a.scrollIntoView && a.parentNode.scrollWidth > a.parentNode.clientWidth) {
          var parent = a.parentNode;
          parent.scrollLeft = a.offsetLeft - parent.clientWidth / 2 + a.clientWidth / 2;
        }
      });
    }, { rootMargin: '-140px 0px -55% 0px' });
    targets.forEach(function (el) { if (el) io.observe(el); });
  }

  /* #t-유형 으로 들어오면 해당 카드로 (수식 렌더링 후 위치 보정) */
  if (window.location.hash) {
    var target = document.getElementById(window.location.hash.slice(1));
    if (target) {
      window.addEventListener('load', function () { target.scrollIntoView({ block: 'start' }); });
    }
  }
})();
