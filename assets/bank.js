/* 문제 은행: bank.html?level=1..4 */
(function () {
  var D = window.CM_DATA;
  var root = document.getElementById('bank');
  if (!D || !root) return;

  var params = new URLSearchParams(window.location.search);
  var level = parseInt(params.get('level'), 10);
  if (!(level >= 1 && level <= 4)) level = 1;
  var meta = D.levels[String(level)];
  var problems = D.problems.filter(function (p) { return p.lv === level; });
  var chapters = [12, 13, 14, 15, 16];
  var progress = CM.load();
  var filter = { ch: 'all', status: 'all' };
  var esc = CM.escapeHtml;

  /* ── 머리말 ── */
  document.title = meta.title + ' · 기초통신수학 II 문제 은행';
  document.getElementById('lv-eyebrow').textContent = meta.eyebrow;
  document.getElementById('lv-title').textContent = meta.title;
  document.getElementById('lv-lead').textContent = meta.lead;
  var perCh = chapters.map(function (c) {
    return problems.filter(function (p) { return p.ch === c; }).length;
  });
  document.getElementById('lv-facts').innerHTML =
    '<span><b>30</b>문제</span>' +
    '<span>' + esc(meta.focus) + '</span>' +
    '<span>' + chapters.map(function (c, i) { return 'Ch.' + c + ' <b>' + perCh[i] + '</b>'; }).join(' &nbsp;') + '</span>';
  var lvLinks = document.querySelectorAll('.levels a');
  for (var i = 0; i < lvLinks.length; i++) {
    if (lvLinks[i].getAttribute('data-level') === String(level)) lvLinks[i].setAttribute('aria-current', 'page');
  }

  /* ── 필터 칩 ── */
  var chGroup = document.getElementById('f-ch');
  chGroup.innerHTML = '<button class="chip" type="button" data-ch="all" aria-pressed="true">전체<span class="cnt">30</span></button>' +
    chapters.map(function (c, i) {
      return '<button class="chip" type="button" data-ch="' + c + '" aria-pressed="false" title="' + esc(D.chapters[c].name) + '">Ch.' + c + '<span class="cnt">' + perCh[i] + '</span></button>';
    }).join('');

  /* ── 문제 카드 ── */
  function card(p) {
    var typeName = D.types[p.type];
    var secName = D.sections[p.sec];
    return '' +
      '<article class="prob" id="p' + p.id + '" data-ch="' + p.ch + '" data-id="' + p.id + '">' +
        '<div class="prob-h">' +
          '<span class="pno">' + p.id + '</span>' +
          '<span class="tag sec">' + p.sec + ' ' + esc(secName) + '</span>' +
          '<a class="tag" href="concepts.html#t-' + p.type + '" title="개념 정리에서 이 유형 보기">' + esc(typeName) + '</a>' +
          '<span class="state" aria-live="polite"></span>' +
        '</div>' +
        '<div class="prob-q">' + p.q + '</div>' +
        '<p class="prob-src">근거: ' + esc(p.src) + '</p>' +
        '<div class="prob-actions">' +
          '<button class="btn" type="button" data-act="hint" aria-expanded="false" aria-controls="h' + p.id + '">힌트</button>' +
          '<button class="btn" type="button" data-act="ans" aria-expanded="false" aria-controls="a' + p.id + '">정답</button>' +
          '<button class="btn" type="button" data-act="sol" aria-expanded="false" aria-controls="s' + p.id + '">풀이</button>' +
          '<span class="grow"></span>' +
          '<button class="mark ok" type="button" data-mark="ok" aria-pressed="false">맞았어요</button>' +
          '<button class="mark retry" type="button" data-mark="retry" aria-pressed="false">다시 풀기</button>' +
        '</div>' +
        '<div class="reveal hint" id="h' + p.id + '" hidden><span class="lbl">힌트</span>' + p.hint + '</div>' +
        '<div class="reveal ans" id="a' + p.id + '" hidden><span class="lbl">정답</span>' + p.ans + '</div>' +
        '<div class="reveal sol" id="s' + p.id + '" hidden><span class="lbl">풀이</span><ol>' +
          p.sol.map(function (line) { return '<li>' + line + '</li>'; }).join('') +
        '</ol></div>' +
      '</article>';
  }

  root.innerHTML = chapters.map(function (c) {
    var list = problems.filter(function (p) { return p.ch === c; });
    var info = D.chapters[c];
    return '<section class="chapter" data-ch="' + c + '" aria-labelledby="ch' + c + '">' +
      '<h2 id="ch' + c + '"><span class="n">' + c + '</span>' + esc(info.name) + '<small>' + esc(info.range) + ' · ' + list.length + '문제</small></h2>' +
      list.map(card).join('') +
      '</section>';
  }).join('') +
  '<div class="empty" id="empty" hidden><p>이 조건에 맞는 문제가 없어요.</p><button class="tool" type="button" id="clear-filter">필터 해제</button></div>';

  CM.renderMath(root);

  /* ── 진행 상황 ── */
  function setCardState(el) {
    var id = el.getAttribute('data-id');
    var st = progress[id];
    el.classList.toggle('is-ok', st === 'ok');
    el.classList.toggle('is-retry', st === 'retry');
    var stateEl = el.querySelector('.state');
    stateEl.className = 'state' + (st ? ' ' + st : '');
    stateEl.textContent = st === 'ok' ? '✓ 맞음' : st === 'retry' ? '↺ 다시 풀기' : '';
    var marks = el.querySelectorAll('[data-mark]');
    for (var j = 0; j < marks.length; j++) {
      marks[j].setAttribute('aria-pressed', marks[j].getAttribute('data-mark') === st ? 'true' : 'false');
    }
  }

  function summary() {
    var ok = 0, retry = 0;
    problems.forEach(function (p) {
      if (progress[p.id] === 'ok') ok++;
      else if (progress[p.id] === 'retry') retry++;
    });
    document.getElementById('p-ok').textContent = ok;
    document.getElementById('p-retry').textContent = retry;
    document.getElementById('pm-ok').textContent = ok;
    document.getElementById('pm-retry').textContent = retry;
    document.getElementById('bar-ok').style.width = (ok / problems.length * 100) + '%';
    document.getElementById('bar-retry').style.width = (retry / problems.length * 100) + '%';
  }

  var cards = root.querySelectorAll('.prob');
  for (var k = 0; k < cards.length; k++) setCardState(cards[k]);
  summary();

  /* ── 필터 적용 ── */
  function applyFilter() {
    var shown = 0;
    for (var a = 0; a < cards.length; a++) {
      var el = cards[a];
      var id = el.getAttribute('data-id');
      var st = progress[id];
      var okCh = filter.ch === 'all' || el.getAttribute('data-ch') === filter.ch;
      var okSt = filter.status === 'all' ||
        (filter.status === 'todo' && !st) ||
        (filter.status === st);
      el.hidden = !(okCh && okSt);
      if (!el.hidden) shown++;
    }
    var secs = root.querySelectorAll('.chapter');
    for (var b = 0; b < secs.length; b++) {
      secs[b].hidden = !secs[b].querySelector('.prob:not([hidden])');
    }
    document.getElementById('empty').hidden = shown !== 0;
    var chips = document.querySelectorAll('[data-ch].chip');
    for (var c = 0; c < chips.length; c++) chips[c].setAttribute('aria-pressed', chips[c].getAttribute('data-ch') === filter.ch ? 'true' : 'false');
    var sts = document.querySelectorAll('[data-status].chip');
    for (var d = 0; d < sts.length; d++) sts[d].setAttribute('aria-pressed', sts[d].getAttribute('data-status') === filter.status ? 'true' : 'false');
  }

  document.querySelector('.filterbar').addEventListener('click', function (e) {
    var chip = e.target.closest('.chip');
    if (chip) {
      if (chip.hasAttribute('data-ch')) filter.ch = chip.getAttribute('data-ch');
      if (chip.hasAttribute('data-status')) filter.status = chip.getAttribute('data-status');
      applyFilter();
    }
  });
  document.getElementById('clear-filter').addEventListener('click', function () {
    filter.ch = 'all'; filter.status = 'all'; applyFilter();
  });

  /* ── 카드 안 버튼 ── */
  root.addEventListener('click', function (e) {
    var btn = e.target.closest('button');
    if (!btn) return;
    var el = btn.closest('.prob');
    if (!el) return;
    var act = btn.getAttribute('data-act');
    if (act) {
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      panel.hidden = !open;
      return;
    }
    var mark = btn.getAttribute('data-mark');
    if (mark) {
      var id = el.getAttribute('data-id');
      if (progress[id] === mark) delete progress[id];
      else progress[id] = mark;
      CM.save(progress);
      setCardState(el);
      summary();
      if (filter.status !== 'all') applyFilter();
    }
  });

  /* ── 모두 펼치기 / 기록 초기화 ── */
  var expandBtn = document.getElementById('expand-all');
  expandBtn.addEventListener('click', function () {
    var open = expandBtn.getAttribute('aria-pressed') !== 'true';
    expandBtn.setAttribute('aria-pressed', open ? 'true' : 'false');
    expandBtn.textContent = open ? '정답·풀이 모두 접기' : '정답·풀이 모두 펼치기';
    var btns = root.querySelectorAll('[data-act="ans"], [data-act="sol"]');
    for (var m = 0; m < btns.length; m++) {
      btns[m].setAttribute('aria-expanded', open ? 'true' : 'false');
      document.getElementById(btns[m].getAttribute('aria-controls')).hidden = !open;
    }
  });

  var resetBtn = document.getElementById('reset');
  var armTimer = null;
  resetBtn.addEventListener('click', function () {
    if (!resetBtn.classList.contains('armed')) {
      resetBtn.classList.add('armed');
      resetBtn.textContent = '한 번 더 누르면 이 단계 기록 삭제';
      armTimer = setTimeout(function () {
        resetBtn.classList.remove('armed');
        resetBtn.textContent = '기록 초기화';
      }, 4000);
      return;
    }
    clearTimeout(armTimer);
    problems.forEach(function (p) { delete progress[p.id]; });
    CM.save(progress);
    for (var n = 0; n < cards.length; n++) setCardState(cards[n]);
    summary();
    applyFilter();
    resetBtn.classList.remove('armed');
    resetBtn.textContent = '기록이 지워졌어요';
    setTimeout(function () { resetBtn.textContent = '기록 초기화'; }, 2000);
  });

  /* ── 아래쪽 이동 링크 ── */
  var nav = document.getElementById('next');
  var parts = [];
  parts.push(level > 1
    ? '<a class="ghost" href="bank.html?level=' + (level - 1) + '">' + (level - 1) + '단계로</a>'
    : '<a class="ghost" href="concepts.html">개념 정리 보기</a>');
  parts.push(level < 4
    ? '<a href="bank.html?level=' + (level + 1) + '">' + (level + 1) + '단계 · ' + esc(D.levels[String(level + 1)].name) + ' 풀기</a>'
    : '<a href="index.html">대시보드로</a>');
  nav.innerHTML = parts.join('');

  /* ── #p1-03 처럼 특정 문제로 들어온 경우 ── */
  function focusHash() {
    var m = /^#p(\d-\d\d)$/.exec(window.location.hash);
    if (!m) return;
    var el = document.getElementById('p' + m[1]);
    if (!el) return;
    if (el.hidden) { filter.ch = 'all'; filter.status = 'all'; applyFilter(); }
    el.scrollIntoView({ block: 'start' });
    el.classList.remove('flash');
    void el.offsetWidth;
    el.classList.add('flash');
  }
  window.addEventListener('hashchange', focusHash);
  if (window.location.hash) {
    if (document.readyState === 'complete') focusHash();
    else window.addEventListener('load', focusHash);
  }
})();
