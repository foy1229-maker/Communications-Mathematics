/* 모의고사: mock.html (예상 모의고사) · mock.html?set=1…5 (실전 모의고사)
   문제 데이터는 assets/mock-problems.js — tools/mock.py · tools/mock_sets.py 에서 생성 */
(function () {
  var D = window.CM_MOCK;
  var root = document.getElementById('mock');
  if (!D || !root) return;

  var sets = D.sets || [];
  var setNo = parseInt(new URLSearchParams(window.location.search).get('set'), 10);
  if (!(setNo >= 1 && setNo <= sets.length)) setNo = 0;
  var S = setNo ? sets[setNo - 1] : null;

  var progress = CM.load();
  var esc = CM.escapeHtml;
  // 풀이 기록 키: 예상 모의고사는 기존 그대로 mock-q1 · mock-x1, 실전 n회는 mock-s{n}-q1 (문제 은행의 1-01 같은 키와 겹치지 않게)
  function keyOf(n, id) { return n ? 'mock-s' + n + '-' + id : 'mock-' + id; }
  function key(id) { return keyOf(setNo, id); }
  var all = S ? S.problems : D.exam.concat(D.extra);

  /* ── 회차 탭 ── */
  function setCounts(n) {
    var list = n ? sets[n - 1].problems : D.exam.concat(D.extra);
    var ok = 0;
    list.forEach(function (q) { if (progress[keyOf(n, q.id)] === 'ok') ok++; });
    return [ok, list.length];
  }
  function renderTabs() {
    var tabs = document.querySelectorAll('#set-tabs a[data-set]');
    for (var i = 0; i < tabs.length; i++) {
      var n = parseInt(tabs[i].getAttribute('data-set'), 10);
      if (n > sets.length) { tabs[i].hidden = true; continue; }
      var c = setCounts(n);
      var sm = tabs[i].querySelector('small');
      if (!sm.hasAttribute('data-label')) sm.setAttribute('data-label', sm.textContent);   // 짧은 이름(표준·2025형 …)은 HTML 그대로
      sm.innerHTML = esc(sm.getAttribute('data-label')) + (c[0] ? ' · <b>' + c[0] + '</b>/' + c[1] : '');
      tabs[i].title = n ? sets[n - 1].title + ' — ' + sets[n - 1].focus : '예상 모의고사 — 예상 유형 10문항 + 추가 5문항';
      tabs[i].classList.toggle('done', c[0] === c[1]);
      if (n === setNo) tabs[i].setAttribute('aria-current', 'page');
      else tabs[i].removeAttribute('aria-current');
    }
  }
  renderTabs();

  /* ── 머리말 (실전 모의고사) ── */
  if (S) {
    document.title = S.title + ' · 기초통신수학 II';
    document.getElementById('mk-eyebrow').textContent = 'MOCK EXAM · SET ' + S.no;
    document.getElementById('mk-title').textContent = S.title;
    document.getElementById('mk-lead').textContent = S.lead;
    document.getElementById('mk-facts').innerHTML =
      '<span><b>10</b>문항 · 각 10점</span><span>' + esc(S.focus) + '</span><span>범위 Ch.12 – 16.4</span><span>계산기 사용 불가</span>';
    document.getElementById('mk-nav').innerHTML =
      '<a class="chip" href="#sec-exam">문항 1 – 10</a><a class="chip" href="#sec-plan">출제 구성</a>';
    document.getElementById('h-exam-t').textContent = S.no + '회 문제';
    document.getElementById('h-exam-s').textContent = '10문항 · 각 10점 · 권장 100분';
    document.getElementById('sec-compare').hidden = true;
    document.getElementById('sec-extra').hidden = true;
    document.getElementById('sec-plan').hidden = false;
  }
  var totals = document.querySelectorAll('.p-total');
  for (var tt = 0; tt < totals.length; tt++) totals[tt].textContent = all.length;

  /* ── 문제 카드 ── */
  function rows(list) {
    return list.map(function (it) {
      return '<div class="arow' + (it[0] ? '' : ' nolab') + '">' +
        (it[0] ? '<span class="pl">(' + it[0] + ')</span>' : '') + '<div>' + it[1] + '</div></div>';
    }).join('');
  }
  function similar(q) {
    if (!q.types || !q.types.length) return '';
    return '<p class="similar"><span>비슷한 문제</span>' + q.types.map(function (t) {
      return '<a href="bank.html?level=4&amp;type=' + encodeURIComponent(t[0]) + '" title="문제 은행에서 이 유형만 보기">' + esc(t[1]) + '</a>';
    }).join('') + '</p>';
  }

  function card(q, isExam) {
    var parts = q.parts.length
      ? '<ol class="qparts">' + q.parts.map(function (p) {
          return '<li><span class="pl">(' + p[0] + ')</span><div>' + p[1] + '</div></li>';
        }).join('') + '</ol>'
      : '';
    var sol = q.solution.map(function (s) {
      return '<section class="ssec">' + (s[0] ? '<h4>(' + s[0] + ')</h4>' : '') +
        '<ol>' + s[1].map(function (line) { return '<li>' + line + '</li>'; }).join('') + '</ol></section>';
    }).join('');
    return '' +
      '<article class="prob mock-q" id="' + q.id + '" data-id="' + q.id + '">' +
        '<div class="prob-h">' +
          '<span class="pno">' + q.no + '</span>' +
          '<span class="tag sec">' + esc(q.type) + '</span>' +
          '<span class="tag">' + esc(q.ref) + '</span>' +
          (isExam ? '<span class="pts">10점</span>' : '') +
          '<span class="state" aria-live="polite"></span>' +
        '</div>' +
        '<div class="prob-q">' + (q.stem ? '<p class="stem">' + q.stem + '</p>' : '') + parts + '</div>' +
        similar(q) +
        '<div class="prob-actions">' +
          '<button class="btn" type="button" data-act="ans" aria-expanded="false" aria-controls="a-' + q.id + '">정답</button>' +
          '<button class="btn" type="button" data-act="sol" aria-expanded="false" aria-controls="s-' + q.id + '">풀이</button>' +
          '<span class="grow"></span>' +
          '<button class="mark ok" type="button" data-mark="ok" aria-pressed="false">맞았어요</button>' +
          '<button class="mark retry" type="button" data-mark="retry" aria-pressed="false">다시 풀기</button>' +
        '</div>' +
        '<div class="reveal ans" id="a-' + q.id + '" hidden><span class="lbl">정답</span>' + rows(q.answer) + '</div>' +
        '<div class="reveal sol" id="s-' + q.id + '" hidden><span class="lbl">풀이</span>' + sol + '</div>' +
      '</article>';
  }

  if (S) {
    document.getElementById('exam-list').innerHTML = S.problems.map(function (q) { return card(q, true); }).join('');
    document.getElementById('plan-lead').textContent = S.lead;
    document.getElementById('plan-cap').textContent = S.title + ' 문항별 구성';
    document.getElementById('plan-body').innerHTML = S.problems.map(function (q) {
      return '<tr><td class="c"><a href="#' + q.id + '">' + q.no + '번</a></td><td>' + esc(q.type) + '</td><td>' + esc(q.ref) + '</td>' +
        '<td>' + similar(q) + '</td></tr>';
    }).join('');
  } else {
    document.getElementById('exam-list').innerHTML = D.exam.map(function (q) { return card(q, true); }).join('');
    document.getElementById('extra-list').innerHTML = D.extra.map(function (q) { return card(q, false); }).join('');
    document.getElementById('map-body').innerHTML = D.map.map(function (m) {
      return '<tr><td class="c">' + m.no + '</td><td>' + m.what + '</td><td class="c num">' + m.sec + '</td>' +
        '<td class="c">' + (m.mine ? esc(m.mine) : '<span class="miss">없음</span>') + '</td>' +
        '<td><a href="#' + m.href + '">' + esc(m.here) + '</a></td></tr>';
    }).join('');
  }
  CM.renderMath(root);

  /* ── 풀이 기록 ── */
  var cards = root.querySelectorAll('.prob');
  function setCardState(el) {
    var st = progress[key(el.getAttribute('data-id'))];
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
    all.forEach(function (q) {
      var st = progress[key(q.id)];
      if (st === 'ok') ok++; else if (st === 'retry') retry++;
    });
    document.getElementById('p-ok').textContent = ok;
    document.getElementById('p-retry').textContent = retry;
    document.getElementById('pm-ok').textContent = ok;
    document.getElementById('pm-retry').textContent = retry;
    document.getElementById('bar-ok').style.width = (ok / all.length * 100) + '%';
    document.getElementById('bar-retry').style.width = (retry / all.length * 100) + '%';
    renderTabs();
  }
  for (var k = 0; k < cards.length; k++) setCardState(cards[k]);
  summary();

  root.addEventListener('click', function (e) {
    var btn = e.target.closest('button');
    if (!btn) return;
    var el = btn.closest('.prob');
    if (!el) return;
    if (btn.hasAttribute('data-act')) {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.getElementById(btn.getAttribute('aria-controls')).hidden = !open;
      return;
    }
    var mark = btn.getAttribute('data-mark');
    if (mark) {
      var id = key(el.getAttribute('data-id'));
      if (progress[id] === mark) delete progress[id];
      else progress[id] = mark;
      CM.save(progress);
      setCardState(el);
      summary();
    }
  });

  /* ── 모두 펼치기 · 유형 이름 가리기 · 기록 초기화 ── */
  var expandBtn = document.getElementById('expand-all');
  expandBtn.addEventListener('click', function () {
    var open = expandBtn.getAttribute('aria-pressed') !== 'true';
    expandBtn.setAttribute('aria-pressed', open ? 'true' : 'false');
    expandBtn.textContent = open ? '정답·풀이 모두 접기' : '정답·풀이 모두 펼치기';
    var btns = root.querySelectorAll('[data-act]');
    for (var m = 0; m < btns.length; m++) {
      btns[m].setAttribute('aria-expanded', open ? 'true' : 'false');
      document.getElementById(btns[m].getAttribute('aria-controls')).hidden = !open;
    }
  });

  var hideBtn = document.getElementById('hide-type');
  hideBtn.addEventListener('click', function () {
    var on = hideBtn.getAttribute('aria-pressed') !== 'true';
    hideBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    document.body.classList.toggle('notype', on);
  });

  var resetBtn = document.getElementById('reset');
  var armTimer = null;
  resetBtn.addEventListener('click', function () {
    if (!resetBtn.classList.contains('armed')) {
      resetBtn.classList.add('armed');
      resetBtn.textContent = '한 번 더 누르면 이 회차 기록 삭제';
      armTimer = setTimeout(function () {
        resetBtn.classList.remove('armed');
        resetBtn.textContent = '기록 초기화';
      }, 4000);
      return;
    }
    clearTimeout(armTimer);
    all.forEach(function (q) { delete progress[key(q.id)]; });
    CM.save(progress);
    for (var n = 0; n < cards.length; n++) setCardState(cards[n]);
    summary();
    resetBtn.classList.remove('armed');
    resetBtn.textContent = '기록이 지워졌어요';
    setTimeout(function () { resetBtn.textContent = '기록 초기화'; }, 2000);
  });

  /* ── 풀이 시간 재기 ── */
  var out = document.getElementById('t-out'), go = document.getElementById('t-go'), clear = document.getElementById('t-reset');
  var spent = 0, since = null, tick = null;
  function pad(x) { return (x < 10 ? '0' : '') + x; }
  function show() {
    var s = Math.floor((spent + (since ? Date.now() - since : 0)) / 1000);
    var h = Math.floor(s / 3600), mm = Math.floor(s % 3600 / 60);
    out.textContent = (h ? h + ':' + pad(mm) : pad(mm)) + ':' + pad(s % 60);
  }
  go.addEventListener('click', function () {
    if (since) { spent += Date.now() - since; since = null; clearInterval(tick); go.textContent = '계속'; }
    else { since = Date.now(); tick = setInterval(show, 250); go.textContent = '멈춤'; clear.disabled = false; }
    go.setAttribute('aria-pressed', since ? 'true' : 'false');
    show();
  });
  clear.addEventListener('click', function () {
    spent = 0;
    if (since) since = Date.now();
    else { go.textContent = '시작'; clear.disabled = true; }
    show();
  });

  /* ── 아래쪽 이동 링크: 다음 회차 ── */
  var nextNav = document.querySelector('nav.next');
  if (nextNav) {
    var nxt = setNo < sets.length ? setNo + 1 : 0;
    nextNav.innerHTML = '<a class="ghost" href="concepts.html">개념 정리 보기</a>' +
      (nxt ? '<a href="mock.html?set=' + nxt + '">실전 모의고사 ' + nxt + '회 풀기</a>' : '<a href="index.html">대시보드로</a>');
  }

  /* ── #q3, #x2 처럼 특정 문항으로 들어온 경우 ── */
  function focusHash() {
    var m = /^#([qx]\d{1,2})$/.exec(window.location.hash);
    if (!m) return;
    var el = document.getElementById(m[1]);
    if (!el) return;
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
