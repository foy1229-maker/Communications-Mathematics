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
      box.innerHTML = '<span>연습</span>' + list.map(function (p) {
        var done = progress[p.id] === 'ok';
        return '<a href="' + CM.bankUrl(p) + '"' + (done ? ' class="done" title="맞은 문제"' : '') + '>' + p.id + '</a>';
      }).join('');
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
