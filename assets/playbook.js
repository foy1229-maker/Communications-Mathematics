/* 풀이 행동강령: 수식 렌더링, 비교 모드(내 강령에도 있는 항목 체크 · 빠진 것만 보기 · 카드별 메모), 연습 링크의 맞은 수, 목차 위치 표시.
   체크와 메모는 이 브라우저(localStorage 'cm2.playbook.v1')에만 저장돼요. 저장이 막힌 환경에서는 이 페이지를 연 동안만 유지돼요. */
(function () {
  var KEY = 'cm2.playbook.v1';
  var memory = null;

  function read() {
    var v = memory;
    try {
      var raw = window.localStorage.getItem(KEY);
      if (raw) v = JSON.parse(raw);
    } catch (e) { /* 저장소를 못 쓰면 메모리 값 */ }
    if (!v || typeof v !== 'object') v = {};
    return {
      have: v.have && typeof v.have === 'object' ? v.have : {},
      memo: v.memo && typeof v.memo === 'object' ? v.memo : {},
      mode: !!v.mode,
      missing: !!v.missing
    };
  }
  var state = read();

  function write() {
    memory = state;
    try { window.localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* 저장 불가: 메모리에만 유지 */ }
  }

  var body = document.body;
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-item]'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('[data-card]'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.pb-g, .pb-col, .pb-sit'));
  var memos = Array.prototype.slice.call(document.querySelectorAll('textarea[data-memo]'));
  var modeBtn = document.getElementById('pb-mode');
  var resetBtn = document.getElementById('pb-reset');
  var printBtn = document.getElementById('pb-print');
  var missingBtns = Array.prototype.slice.call(document.querySelectorAll('[data-act="missing"]'));
  var offBtns = Array.prototype.slice.call(document.querySelectorAll('[data-act="off"]'));
  var floatBar = document.querySelector('.pb-float');
  var totalEls = Array.prototype.slice.call(document.querySelectorAll('[data-total-have]'));

  /* 항목마다 체크 버튼 (비교 모드에서만 보여요) */
  items.forEach(function (el) {
    var host = el;
    if (el.tagName === 'TR') host = el.querySelector('td');
    else if (el.classList.contains('pb-table')) host = el.querySelector('.pb-cap');
    if (!host) return;
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'pb-ck';
    b.setAttribute('aria-pressed', 'false');
    b.setAttribute('aria-label', '내 강령에도 있음');
    b.title = '내 강령에도 있음';
    host.insertBefore(b, host.firstChild);
  });

  function hasMemo() {
    for (var k in state.memo) {
      if (Object.prototype.hasOwnProperty.call(state.memo, k) && state.memo[k]) return true;
    }
    return false;
  }

  function countHave(list) {
    var n = 0;
    for (var i = 0; i < list.length; i++) if (state.have[list[i].getAttribute('data-item')]) n++;
    return n;
  }

  function apply() {
    var total = 0;
    items.forEach(function (el) {
      var on = !!state.have[el.getAttribute('data-item')];
      el.classList.toggle('have', on);
      var b = el.querySelector('.pb-ck');
      if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false');
      if (on) total++;
    });
    groups.forEach(function (g) {
      var its = g.querySelectorAll('[data-item]');
      g.classList.toggle('all', its.length > 0 && countHave(its) === its.length);
    });
    cards.forEach(function (c) {
      var its = c.querySelectorAll('[data-item]');
      var n = countHave(its);
      var cnt = c.querySelector('.pb-cnt');
      if (cnt) cnt.textContent = state.mode ? '있음 ' + n + ' / ' + its.length : '';
      c.classList.toggle('done', its.length > 0 && n === its.length);
    });
    body.classList.toggle('pb-compare', state.mode);
    body.classList.toggle('pb-missing', state.mode && state.missing);
    totalEls.forEach(function (el) { el.textContent = total; });
    if (modeBtn) {
      modeBtn.setAttribute('aria-pressed', state.mode ? 'true' : 'false');
      modeBtn.textContent = state.mode ? '비교 모드 끄기' : '비교 모드 켜기';
    }
    missingBtns.forEach(function (b) {
      b.disabled = !state.mode;
      b.setAttribute('aria-pressed', state.mode && state.missing ? 'true' : 'false');
    });
    if (floatBar) floatBar.hidden = !state.mode;
    if (resetBtn) resetBtn.disabled = !(total || hasMemo());
  }

  /* 메모: 저장된 내용 채우기, 입력할 때마다 저장(조금 모아서) */
  function syncMemoBox(ta) {
    var box = ta.parentNode;
    var v = ta.value.trim();
    box.classList.toggle('has', !!v);
    var pr = box.querySelector('.pb-memo-print');
    if (pr) pr.textContent = v;
  }
  var memoTimer = null;
  memos.forEach(function (ta) {
    var id = ta.getAttribute('data-memo');
    ta.value = typeof state.memo[id] === 'string' ? state.memo[id] : '';
    syncMemoBox(ta);
    ta.addEventListener('input', function () {
      var v = ta.value;
      if (v.trim()) state.memo[id] = v; else delete state.memo[id];
      syncMemoBox(ta);
      if (resetBtn) resetBtn.disabled = !(countHave(items) || hasMemo());
      clearTimeout(memoTimer);
      memoTimer = setTimeout(write, 300);
    });
  });
  window.addEventListener('pagehide', function () { if (memoTimer) { clearTimeout(memoTimer); write(); } });

  /* 클릭: 항목 체크 · 모드 · 빠진 것만 · 끄기 */
  document.addEventListener('click', function (ev) {
    var t = ev.target;
    if (!t || !t.closest) return;
    var ck = t.closest('.pb-ck');
    if (ck) {
      var item = ck.closest('[data-item]');
      if (!item) return;
      var id = item.getAttribute('data-item');
      if (state.have[id]) delete state.have[id]; else state.have[id] = 1;
      write();
      apply();
      return;
    }
    if (t.closest('#pb-mode')) {
      state.mode = !state.mode;
      write();
      apply();
      return;
    }
    if (t.closest('[data-act="missing"]')) {
      if (!state.mode) return;
      state.missing = !state.missing;
      write();
      apply();
      return;
    }
    if (t.closest('[data-act="off"]')) {
      state.mode = false;
      write();
      apply();
    }
  });

  /* 체크·메모 지우기: 두 번 눌러 확인 (첫 번째 누름에서 버튼이 빨개지고 4초 안에 다시 누르면 지워요) */
  if (resetBtn) {
    var armTimer = null;
    var label = resetBtn.textContent;
    resetBtn.addEventListener('click', function () {
      if (!resetBtn.classList.contains('armed')) {
        resetBtn.classList.add('armed');
        resetBtn.textContent = '한 번 더 누르면 지워요';
        armTimer = setTimeout(function () { resetBtn.classList.remove('armed'); resetBtn.textContent = label; }, 4000);
        return;
      }
      clearTimeout(armTimer);
      resetBtn.classList.remove('armed');
      resetBtn.textContent = label;
      state.have = {};
      state.memo = {};
      state.missing = false;
      memos.forEach(function (ta) { ta.value = ''; syncMemoBox(ta); });
      write();
      apply();
    });
  }
  if (printBtn) printBtn.addEventListener('click', function () { window.print(); });

  /* 연습 링크: 그 단계·유형 문제 중 맞은 수 (문제 은행 기록) */
  var progress = window.CM ? CM.load() : {};
  var plinks = document.querySelectorAll('.pb-practice a[data-ids]');
  for (var i = 0; i < plinks.length; i++) {
    var ids = plinks[i].getAttribute('data-ids').split(' ');
    var done = ids.filter(function (id) { return progress[id] === 'ok'; }).length;
    if (!done) continue;
    var sp = plinks[i].querySelector('span');
    if (sp) sp.textContent = done + '/' + ids.length;
    if (done === ids.length) plinks[i].classList.add('done');
  }

  apply();

  if (window.CM) {
    CM.renderMath(document.querySelector('main'));
    CM.renderMath(document.querySelector('.hero'));
  }

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
        if (on && a.parentNode.scrollWidth > a.parentNode.clientWidth) {
          var parent = a.parentNode;
          parent.scrollLeft = a.offsetLeft - parent.clientWidth / 2 + a.clientWidth / 2;
        }
      });
    }, { rootMargin: '-140px 0px -55% 0px' });
    targets.forEach(function (el) { if (el) io.observe(el); });
  }

  /* #p-15-sph 처럼 카드로 들어오면 수식 렌더링 뒤 위치 보정 */
  if (window.location.hash) {
    var target = document.getElementById(window.location.hash.slice(1));
    if (target) {
      window.addEventListener('load', function () { target.scrollIntoView({ block: 'start' }); });
    }
  }
})();
