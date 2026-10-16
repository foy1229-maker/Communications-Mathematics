/* 모의고사: mock.html?set=1 (A세트) · mock.html?set=2 (B세트) — 주소에 set 이 없으면 A세트
   문제 데이터는 assets/mock-problems.js — tools/mock_sets.py 에서 tools/build.py 로 생성 */
(function () {
  var D = window.CM_MOCK;
  var root = document.getElementById('mock');
  if (!D || !root || !D.sets || !D.sets.length) return;

  var sets = D.sets;
  var setNo = parseInt(new URLSearchParams(window.location.search).get('set'), 10);
  if (!(setNo >= 1 && setNo <= sets.length)) setNo = 1;
  var S = sets[setNo - 1];
  var all = S.problems;

  var progress = CM.load();
  var esc = CM.escapeHtml;
  // 풀이 기록 키: mock-a-q1 … mock-a-q10, mock-b-q1 … (예전 예상·실전 모의고사 키 mock-q1 · mock-s1-q1 과 겹치지 않게)
  function keyOf(set, id) { return 'mock-' + set.id + '-' + id; }
  function key(id) { return keyOf(S, id); }

  /* ── 세트 탭 ── */
  function setCounts(set) {
    var ok = 0;
    set.problems.forEach(function (q) { if (progress[keyOf(set, q.id)] === 'ok') ok++; });
    return [ok, set.problems.length];
  }
  function renderTabs() {
    var tabs = document.querySelectorAll('#set-tabs a[data-set]');
    for (var i = 0; i < tabs.length; i++) {
      var n = parseInt(tabs[i].getAttribute('data-set'), 10);
      var set = sets[n - 1];
      if (!set) { tabs[i].hidden = true; continue; }
      var c = setCounts(set);
      var sm = tabs[i].querySelector('small');
      sm.innerHTML = esc(set.mins + '분') + (c[0] ? ' · <b>' + c[0] + '</b>/' + c[1] : '');
      tabs[i].title = set.title + ' — ' + set.focus;
      tabs[i].classList.toggle('done', c[0] === c[1]);
      if (n === setNo) tabs[i].setAttribute('aria-current', 'page');
      else tabs[i].removeAttribute('aria-current');
    }
  }
  renderTabs();

  /* ── 머리말 ── */
  document.title = S.title + ' · 기초통신수학 II';
  document.getElementById('mk-eyebrow').textContent = 'MOCK EXAM · SET ' + S.label;
  document.getElementById('mk-title').textContent = '중간고사 ' + S.title;
  document.getElementById('mk-lead').textContent = S.lead;
  document.getElementById('mk-facts').innerHTML =
    '<span><b>10</b>문항 · 각 10점</span>' +
    '<span>권장 <b>' + S.mins + '</b>분 (시험 75 – 90분)</span>' +
    '<span>15개 주제 모두 포함</span>' +
    '<span>범위 Ch.12 – 16.4</span>' +
    '<span>계산기 사용 불가</span>';
  document.getElementById('h-exam-t').textContent = S.label + '세트 문제';
  document.getElementById('h-exam-s').textContent = '10문항 · 각 10점 · 권장 ' + S.mins + '분';
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
  function topicNos(q) {
    return q.topics.map(function (t) { return t[0]; }).join(' · ');
  }

  function card(q) {
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
          '<span class="tag">권장 ' + q.mins + '분</span>' +
          '<span class="pts">10점</span>' +
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

  document.getElementById('exam-list').innerHTML = all.map(card).join('');

  /* ── 출제 구성: 문항별 표 + 15개 주제 → 문항 ── */
  document.getElementById('plan-lead').textContent =
    '시험에 꼭 나올 15개 주제를 10문항에 모두 담았어요. 소문항마다 배점을 적어 두었고, 권장 시간 합은 ' + S.mins +
    '분이에요. 단원 순서는 일부러 섞었어요.';
  document.getElementById('plan-cap').textContent = S.title + ' 문항별 구성';
  document.getElementById('plan-body').innerHTML = all.map(function (q) {
    return '<tr><td class="c"><a href="#' + q.id + '">' + q.no + '번</a></td><td>' + esc(q.type) + '</td>' +
      '<td class="c num">' + esc(topicNos(q)) + '</td><td class="c num">' + esc(q.ref) + '</td>' +
      '<td class="c num">' + q.mins + '분</td>' +
      '<td>' + (similar(q) || '<span class="muted">문제 은행에 없는 유형</span>') + '</td></tr>';
  }).join('');
  document.getElementById('topic-cap').textContent = S.title + ' — 15개 주제가 들어간 문항';
  document.getElementById('topic-body').innerHTML = (D.topics || []).map(function (tp) {
    var where = all.filter(function (q) {
      return q.topics.some(function (t) { return t[0] === tp[0]; });
    }).map(function (q) { return '<a href="#' + q.id + '">' + q.no + '번</a>'; });
    return '<tr><td class="c num">' + tp[0] + '</td><td>' + esc(tp[1]) + '</td><td>' +
      (where.length ? where.join(', ') : '<span class="muted">없음</span>') + '</td></tr>';
  }).join('');

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
      resetBtn.textContent = '한 번 더 누르면 이 세트 기록 삭제';
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

  /* ── 아래쪽 이동 링크: 다음 세트 ── */
  var nextNav = document.querySelector('nav.next');
  if (nextNav) {
    var nxt = setNo < sets.length ? sets[setNo] : null;
    nextNav.innerHTML = '<a class="ghost" href="concepts.html">개념 정리 보기</a>' +
      (nxt ? '<a href="mock.html?set=' + (setNo + 1) + '">' + esc(nxt.title) + ' 풀기</a>' : '<a href="index.html">대시보드로</a>');
  }

  /* ── #q3 처럼 특정 문항으로 들어온 경우 ── */
  function focusHash() {
    var m = /^#(q\d{1,2})$/.exec(window.location.hash);
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
