/* 로그인 상태 — 모든 페이지 <head>에서 스타일시트보다 먼저(동기) 불러와요.
   서버가 없는 정적 사이트라 계정 · 로그인 상태 · 풀이 기록은 모두 이 브라우저에만 저장돼요.
   - 로그인하지 않고 대시보드 · 개념 정리 · 문제 은행을 열면 login.html?next=… 로 보내요.
   - 이미 로그인했는데 login.html을 열면 바로 next(없으면 대시보드)로 보내요.
   - 저장 공간이나 암호화 기능을 쓸 수 없는 브라우저에서는 막지 않고 그냥 열어 둬요.
   - [data-user-menu] 자리에 사용자 메뉴(이름 + 로그아웃)를 그려요. */
(function () {
  'use strict';
  var ACCOUNTS = 'cm2.accounts.v1';
  var SESSION = 'cm2.session.v1';
  var PROGRESS = 'cm2.progress.v1';
  var COOKIE = 'cm2_session';
  var KEEP_DAYS = 30;

  var store = (function () {
    try {
      var s = window.localStorage, k = 'cm2.probe';
      s.setItem(k, '1'); s.removeItem(k);
      return s;
    } catch (e) { return null; }
  })();
  var enabled = !!(store && window.crypto && window.crypto.subtle && window.TextEncoder);

  function parse(raw) {
    try { return raw ? JSON.parse(raw) : null; } catch (e) { return null; }
  }

  function accounts() {
    var a = store && parse(store.getItem(ACCOUNTS));
    return a && a.users ? a : { v: 1, users: {} };
  }
  function saveAccounts(a) { store.setItem(ACCOUNTS, JSON.stringify(a)); }

  /* '로그인 상태 유지'를 고르지 않으면 브라우저를 닫을 때 사라지는 쿠키에 담아요 (탭끼리는 공유) */
  var secure = location.protocol === 'https:' ? '; Secure' : '';
  function cookieGet() {
    var m = document.cookie.match(new RegExp('(?:^|; )' + COOKIE + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }
  function cookieSet(v) {
    try { document.cookie = COOKIE + '=' + encodeURIComponent(v) + '; SameSite=Lax' + secure; } catch (e) { return false; }
    return cookieGet() === v;
  }
  function cookieDel() {
    try { document.cookie = COOKIE + '=; Max-Age=0; SameSite=Lax' + secure; } catch (e) { /* 무시 */ }
  }

  function readSession() {
    var s = parse(store.getItem(SESSION));
    if (s && !(s.exp > Date.now())) { store.removeItem(SESSION); s = null; }
    if (!s) s = parse(cookieGet());
    if (!s) { try { s = parse(window.sessionStorage.getItem(SESSION)); } catch (e) { s = null; } }
    return s && typeof s.id === 'string' ? s : null;
  }
  function clear() {
    if (store) store.removeItem(SESSION);
    cookieDel();
    try { window.sessionStorage.removeItem(SESSION); } catch (e) { /* 무시 */ }
  }

  function current() {
    if (!enabled) return null;
    var s = readSession();
    if (!s) return null;
    var u = accounts().users[s.id];
    if (!u) { clear(); return null; }
    return { id: u.id, name: u.name, created: u.created };
  }

  /* 로그인 시작. keep이면 30일 동안 유지, 아니면 브라우저를 닫을 때까지 */
  function start(id, keep) {
    clear();
    var s = JSON.stringify(keep ? { id: id, exp: Date.now() + KEEP_DAYS * 864e5 } : { id: id });
    if (keep) store.setItem(SESSION, s);
    else if (!cookieSet(s)) { try { window.sessionStorage.setItem(SESSION, s); } catch (e) { /* 무시 */ } }
    adoptLegacyProgress(id);
  }

  /* 로그인 기능이 생기기 전에 계정 구분 없이 저장된 기록은 처음 로그인한 계정으로 옮겨요 */
  function adoptLegacyProgress(id) {
    var old = parse(store.getItem(PROGRESS));
    if (!old) return;
    var key = PROGRESS + ':' + id;
    var mine = parse(store.getItem(key)) || {};
    for (var k in old) {
      if (Object.prototype.hasOwnProperty.call(old, k) && !Object.prototype.hasOwnProperty.call(mine, k)) mine[k] = old[k];
    }
    store.setItem(key, JSON.stringify(mine));
    store.removeItem(PROGRESS);
  }

  /* 풀이 기록은 계정마다 따로 */
  function progressKey() {
    var u = current();
    return u ? PROGRESS + ':' + u.id : PROGRESS;
  }

  /* 로그인 뒤 돌아갈 주소는 이 사이트 페이지만 허용 */
  function safeNext(n) {
    return typeof n === 'string' && /^(index|concepts|bank)\.html(\?[\w=&%.-]*)?(#[\w-]*)?$/.test(n) ? n : 'index.html';
  }

  function logout() {
    clear();
    location.replace('login.html?out=1');
  }

  /* ── 문지기 ── */
  var page = location.pathname.split('/').pop() || 'index.html';
  var onLogin = page === 'login.html';
  function go(url) {
    document.documentElement.style.visibility = 'hidden';   // 넘어가기 전 화면이 비치지 않게
    location.replace(url);
  }
  if (enabled) {
    if (!onLogin && !current()) go('login.html?next=' + encodeURIComponent(page + location.search + location.hash));
    else if (onLogin && current()) go(safeNext(new URLSearchParams(location.search).get('next')));
  }

  /* ── 사용자 메뉴 ── */
  function userMenu() {
    var slot = document.querySelector('[data-user-menu]');
    var u = current();
    if (!slot || !u) return;
    slot.classList.add('um');
    slot.innerHTML =
      '<button class="um-btn" type="button" aria-expanded="false" aria-controls="um-panel">' +
        '<span class="um-av" aria-hidden="true"></span><span class="um-name"></span>' +
        '<svg class="um-caret" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M3 4.5 6 7.5 9 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
      '</button>' +
      '<div class="um-panel" id="um-panel" hidden>' +
        '<p class="um-who"><b></b><span></span></p>' +
        '<button class="um-out" type="button">로그아웃</button>' +
      '</div>';
    var btn = slot.querySelector('.um-btn');
    var panel = slot.querySelector('.um-panel');
    slot.querySelector('.um-av').textContent = Array.from(u.name.trim())[0] || '?';
    slot.querySelector('.um-name').textContent = u.name;
    btn.setAttribute('aria-label', u.name + ' 계정 메뉴');
    panel.querySelector('b').textContent = u.name;
    panel.querySelector('span').textContent = '아이디 ' + u.id;

    function open(on) {
      panel.hidden = !on;
      btn.setAttribute('aria-expanded', on ? 'true' : 'false');
    }
    btn.addEventListener('click', function () { open(panel.hidden); });
    panel.querySelector('.um-out').addEventListener('click', logout);
    document.addEventListener('click', function (e) {
      if (!panel.hidden && !slot.contains(e.target)) open(false);
    });
    slot.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !panel.hidden) { open(false); btn.focus(); }
    });
    slot.addEventListener('focusout', function (e) {
      if (!panel.hidden && e.relatedTarget && !slot.contains(e.relatedTarget)) open(false);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', userMenu);
  else userMenu();

  window.CM_SESSION = {
    enabled: enabled,
    accounts: accounts,
    saveAccounts: saveAccounts,
    current: current,
    start: start,
    logout: logout,
    progressKey: progressKey,
    safeNext: safeNext
  };
})();
