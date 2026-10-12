/* 로그인 · 회원가입 · 아이디 찾기 · 비밀번호 찾기 (login.html)
   - 계정은 이 브라우저(localStorage)에만 저장해요. 비밀번호는 PBKDF2-SHA256 해시로, 휴대폰 번호는
     SHA-256 해시와 가린 번호(010-****-1234)로만 남겨요.
   - 휴대폰 인증은 데모예요. 실제 문자 대신 화면 위 알림으로 인증번호를 보여 줘요. (3분 유효, 5번 틀리면 다시 받기)
   - 휴대폰 번호 하나에 계정 하나. 그래서 아이디 찾기는 이름 + 휴대폰 번호로 정확히 하나를 찾아요. */
(function () {
  'use strict';
  var S = window.CM_SESSION;

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  var VIEWS = ['login', 'signup', 'find-id', 'find-pw'];
  var TITLES = { login: '로그인', signup: '회원가입', 'find-id': '아이디 찾기', 'find-pw': '비밀번호 찾기' };

  /* 계정 기능을 쓸 수 없는 브라우저: 로그인 없이 들어가게 */
  if (!S || !S.enabled) {
    VIEWS.forEach(function (v) { $('#view-' + v).hidden = true; });
    $('#view-off').hidden = false;
    return;
  }

  var params = new URLSearchParams(location.search);
  var next = S.safeNext(params.get('next'));
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 암호화 도구 ── */
  var te = new TextEncoder();
  var ITER = 150000;
  function toB64(buf) {
    var b = new Uint8Array(buf), s = '';
    for (var i = 0; i < b.length; i++) s += String.fromCharCode(b[i]);
    return btoa(s);
  }
  function fromB64(s) {
    var bin = atob(s), b = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) b[i] = bin.charCodeAt(i);
    return b;
  }
  function toHex(buf) {
    return Array.prototype.map.call(new Uint8Array(buf), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
  }
  function randomBytes(n) { var a = new Uint8Array(n); crypto.getRandomValues(a); return a; }
  function derive(pw, salt, iter) {
    return crypto.subtle.importKey('raw', te.encode(pw), 'PBKDF2', false, ['deriveBits'])
      .then(function (key) { return crypto.subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt: salt, iterations: iter }, key, 256); })
      .then(toB64);
  }
  function makeSecret(pw) {
    var salt = randomBytes(16);
    return derive(pw, salt, ITER).then(function (hash) { return { salt: toB64(salt), hash: hash, iter: ITER }; });
  }
  function checkSecret(u, pw) {
    return derive(pw, fromB64(u.salt), u.iter || ITER).then(function (h) { return h === u.hash; });
  }
  function phoneHash(d) {
    return crypto.subtle.digest('SHA-256', te.encode('cm2|phone|' + d)).then(toHex);
  }
  function sixDigits() {
    return String(crypto.getRandomValues(new Uint32Array(1))[0] % 1000000).padStart(6, '0');
  }

  /* ── 입력 규칙 ── */
  var ID_HINT = '영문 소문자로 시작하는 4~16자 (영문 소문자 · 숫자 · _)';
  function cleanName(v) { return v.trim().replace(/\s+/g, ' '); }
  function nameOk(v) { return v.length >= 2 && v.length <= 20 && /^[가-힣a-zA-Z]+( [가-힣a-zA-Z]+)*$/.test(v); }
  function idOk(v) { return /^[a-z][a-z0-9_]{3,15}$/.test(v); }
  function pwRules(pw) {
    var kinds = (/[A-Za-z]/.test(pw) ? 1 : 0) + (/\d/.test(pw) ? 1 : 0) + (/[^A-Za-z\d\s]/.test(pw) ? 1 : 0);
    return { len: pw.length >= 8 && pw.length <= 20, mix: kinds >= 2, space: /\s/.test(pw) };
  }
  function pwOk(pw) { var r = pwRules(pw); return r.len && r.mix && !r.space; }
  function digits(v) {
    var d = v.replace(/\D/g, '');
    if (/^821\d{8,9}/.test(d)) d = '0' + d.slice(2);   // +82 10-…
    return d.slice(0, 11);
  }
  function phoneOk(d) { return /^010\d{8}$/.test(d) || /^01[16789]\d{7,8}$/.test(d); }
  function formatPhone(d) {
    var mid = d.length === 10 && d.indexOf('010') !== 0 ? 3 : 4;   // 011-123-4567 / 010-1234-5678
    if (d.length <= 3) return d;
    if (d.length <= 3 + mid) return d.slice(0, 3) + '-' + d.slice(3);
    return d.slice(0, 3) + '-' + d.slice(3, 3 + mid) + '-' + d.slice(3 + mid);
  }
  function maskPhone(d) { return d.slice(0, 3) + '-****-' + d.slice(-4); }
  function users() { return S.accounts().users; }
  function findByPhone(h) {
    var all = users();
    for (var k in all) if (Object.prototype.hasOwnProperty.call(all, k) && all[k].phone === h) return all[k];
    return null;
  }
  function dateKo(t) {
    var d = new Date(t);
    return d.getFullYear() + '년 ' + (d.getMonth() + 1) + '월 ' + d.getDate() + '일';
  }

  /* ── 화면 도우미 ── */
  function setMsg(el, text, kind) {
    el.textContent = text || '';
    el.className = 'msg' + (kind ? ' ' + kind : '');
  }
  function mark(input, bad) { input.setAttribute('aria-invalid', bad ? 'true' : 'false'); }
  function announce(text) {
    var live = $('#sr-live');
    live.textContent = '';
    setTimeout(function () { live.textContent = text; }, 30);
  }
  function busy(btn, on, label) {
    if (on) { btn.dataset.label = btn.textContent; btn.textContent = label; btn.disabled = true; }
    else { btn.textContent = btn.dataset.label || btn.textContent; btn.disabled = false; }
  }

  /* 비밀번호 보기 / Caps Lock 안내 */
  $$('.eye').forEach(function (btn) {
    var input = document.getElementById(btn.getAttribute('aria-controls'));
    btn.addEventListener('click', function () {
      var show = input.type === 'password';
      input.type = show ? 'text' : 'password';
      btn.setAttribute('aria-pressed', show ? 'true' : 'false');
      btn.setAttribute('aria-label', show ? '비밀번호 숨기기' : '비밀번호 보기');
      input.focus();
    });
  });
  $$('input[type="password"]').forEach(function (input) {
    var hint = document.getElementById(input.id + '-caps');
    if (!hint) return;
    function check(e) { if (e.getModifierState) hint.hidden = !e.getModifierState('CapsLock'); }
    input.addEventListener('keydown', check);
    input.addEventListener('keyup', check);
    input.addEventListener('blur', function () { hint.hidden = true; });
  });

  /* 아이디 칸: 영문 대문자는 소문자로 바꿔 줌 (한글 입력 중에는 건드리지 않음) */
  function lowerOnType(input) {
    input.addEventListener('input', function (e) {
      if (e.isComposing) return;
      var v = input.value, low = v.toLowerCase();
      if (v === low) return;
      var p = input.selectionStart;
      input.value = low;
      try { input.setSelectionRange(p, p); } catch (err) { /* 무시 */ }
    });
  }
  ['#li-id', '#su-id', '#fp-id'].forEach(function (sel) { lowerOnType($(sel)); });

  /* 휴대폰 번호 칸: 숫자만, 하이픈 자동 (커서 위치 유지) */
  function bindPhone(input) {
    input.addEventListener('input', function () {
      var pos = input.selectionStart == null ? input.value.length : input.selectionStart;
      var before = digits(input.value.slice(0, pos)).length;
      var f = formatPhone(digits(input.value));
      input.value = f;
      var i = 0, seen = 0;
      while (i < f.length && seen < before) { if (/\d/.test(f.charAt(i))) seen++; i++; }
      try { input.setSelectionRange(i, i); } catch (err) { /* 무시 */ }
    });
  }

  /* 비밀번호 조건 목록 */
  function bindRules(input, list) {
    input.addEventListener('input', function () {
      var r = pwRules(input.value);
      $('[data-rule="len"]', list).classList.toggle('ok', r.len);
      $('[data-rule="mix"]', list).classList.toggle('ok', r.mix);
    });
  }
  function resetRules(list) { $$('li', list).forEach(function (li) { li.classList.remove('ok'); }); }

  /* 비밀번호 확인 칸 */
  function bindConfirm(pw, pw2, msg) {
    function check() {
      if (!pw2.value) { setMsg(msg, ''); mark(pw2, false); return; }
      if (pw2.value === pw.value) { setMsg(msg, '비밀번호가 같아요.', 'ok'); mark(pw2, false); }
      else if (pw2.value.length >= pw.value.length) { setMsg(msg, '비밀번호가 서로 달라요.', 'err'); mark(pw2, true); }
      else { setMsg(msg, ''); mark(pw2, false); }
    }
    pw.addEventListener('input', check);
    pw2.addEventListener('input', check);
  }

  /* ── 데모 문자 알림 ── */
  var sms = (function () {
    var box = $('#sms'), body = $('#sms-body');
    var onFill = null, hideTimer = null;
    $('#sms-fill').addEventListener('click', function () { var f = onFill; hide(); if (f) f(); });
    $('#sms-close').addEventListener('click', hide);
    function show(lines, code, fill) {
      body.textContent = '';
      body.appendChild(document.createTextNode(lines[0] + '\n' + lines[1]));
      var nw = document.createElement('span'); nw.className = 'nw';   // 인증번호와 '입니다.'가 줄에서 갈라지지 않게
      var b = document.createElement('b'); b.textContent = '[' + code + ']';
      nw.appendChild(b);
      nw.appendChild(document.createTextNode(lines[2]));
      body.appendChild(nw);
      body.appendChild(document.createTextNode(lines[3]));
      onFill = fill;
      clearTimeout(hideTimer);
      box.hidden = false;
      box.classList.remove('in');
      void box.offsetWidth;   // 다시 내려오는 움직임
      box.classList.add('in');
    }
    function hide() {
      onFill = null;
      box.classList.remove('in');
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function () { box.hidden = true; }, reduceMotion ? 0 : 450);
    }
    return { show: show, hide: hide };
  })();

  /* ── 휴대폰 인증 한 묶음: 번호 → 인증번호 받기 → 6자리 → 확인 ── */
  function PhoneVerify(root, opts) {
    var phone = $('[data-phone]', root), send = $('[data-send]', root);
    var codeRow = $('[data-code-row]', root), code = $('[data-code]', root);
    var check = $('[data-check]', root), timer = $('[data-timer]', root), msg = $('[data-msg]', root);
    var sent = null, verified = null, tick = null;
    bindPhone(phone);

    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function stop() { clearInterval(tick); tick = null; }
    function showTime() {
      var left = Math.max(0, Math.ceil((sent.exp - Date.now()) / 1000));
      timer.textContent = pad(Math.floor(left / 60)) + ':' + pad(left % 60);
      if (!left) expire('인증 시간이 지났어요. 인증번호를 다시 받으세요.');
    }
    function expire(text) {
      stop();
      if (sent) sent.dead = true;
      timer.textContent = '00:00';
      timer.classList.add('over');
      setMsg(msg, text, 'err');
      sms.hide();
    }
    function reset() {
      stop();
      sent = null; verified = null;
      phone.readOnly = false; phone.value = ''; mark(phone, false);
      send.textContent = '인증번호 받기'; send.disabled = false;
      codeRow.hidden = true; code.value = ''; mark(code, false);
      timer.classList.remove('over');
      root.classList.remove('is-done');
      setMsg(msg, '');
    }
    function unlockPhone() {
      verified = null;
      phone.readOnly = false;
      send.textContent = '인증번호 받기';
      root.classList.remove('is-done');
      setMsg(msg, '');
      if (opts.onReset) opts.onReset();
      phone.focus();
    }

    send.addEventListener('click', function () {
      if (verified) { unlockPhone(); return; }   // '번호 바꾸기'
      var d = digits(phone.value);
      if (!phoneOk(d)) {
        mark(phone, true);
        setMsg(msg, '휴대폰 번호를 정확히 입력하세요. 예: 010-1234-5678', 'err');
        phone.focus();
        return;
      }
      mark(phone, false);
      send.disabled = true;
      Promise.resolve(opts.precheck ? opts.precheck(d) : null).then(function (problem) {
        send.disabled = false;
        if (problem) { if (typeof problem === 'string') setMsg(msg, problem, 'err'); return; }
        var c = sixDigits();
        sent = { d: d, code: c, exp: Date.now() + 180000, tries: 0 };
        send.textContent = '다시 받기';
        codeRow.hidden = false; code.value = ''; mark(code, false);
        timer.classList.remove('over');
        stop(); showTime(); tick = setInterval(showTime, 1000);
        setMsg(msg, '인증번호를 보냈어요. 3분 안에 입력하세요.');
        sms.show(['[Web발신]', '[기통수2 문제 은행] ' + opts.label + ' 인증번호는 ', '입니다.', ' 3분 안에 입력해 주세요.'], c, function () {
          code.value = c;
          code.focus();
        });
        announce('데모 문자 도착. 인증번호 ' + c.split('').join(' '));
        code.focus();
      }).catch(function () {
        send.disabled = false;
        setMsg(msg, '인증번호를 만들지 못했어요. 잠시 뒤 다시 눌러 주세요.', 'err');
      });
    });

    function verify() {
      if (!sent) return;
      if (sent.dead || Date.now() > sent.exp) {
        expire(sent.tries >= 5 ? '인증번호를 5번 틀렸어요. 인증번호를 다시 받으세요.' : '인증 시간이 지났어요. 인증번호를 다시 받으세요.');
        return;
      }
      var v = code.value.replace(/\D/g, '');
      if (v.length !== 6) { mark(code, true); setMsg(msg, '인증번호 6자리를 입력하세요.', 'err'); code.focus(); return; }
      if (v !== sent.code) {
        sent.tries++;
        mark(code, true);
        if (sent.tries >= 5) { expire('인증번호를 5번 틀렸어요. 인증번호를 다시 받으세요.'); return; }
        setMsg(msg, '인증번호가 맞지 않아요. (' + sent.tries + '/5)', 'err');
        code.select();
        return;
      }
      stop();
      verified = sent.d; sent = null;
      phone.readOnly = true;
      codeRow.hidden = true; mark(code, false);
      send.textContent = '번호 바꾸기';
      root.classList.add('is-done');
      setMsg(msg, '휴대폰 인증을 마쳤어요.', 'ok');
      sms.hide();
      if (opts.onVerified) opts.onVerified(verified);
    }
    check.addEventListener('click', verify);
    code.addEventListener('input', function () { code.value = code.value.replace(/\D/g, '').slice(0, 6); mark(code, false); });
    code.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); verify(); } });
    phone.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); if (!verified) send.click(); } });
    phone.addEventListener('input', function () {
      mark(phone, false);
      if (sent && digits(phone.value) !== sent.d) {   // 번호를 바꾸면 보낸 인증번호는 무효
        stop(); sent = null;
        codeRow.hidden = true;
        send.textContent = '인증번호 받기';
        setMsg(msg, '');
        sms.hide();
      }
    });

    return {
      reset: reset,
      stop: stop,
      verified: function () { return verified; },
      fail: function (text) { setMsg(msg, text, 'err'); mark(phone, true); phone.focus(); }
    };
  }

  /* ── 화면 전환 (#login · #signup · #find-id · #find-pw) ── */
  var pending = null;   // 다른 화면에서 넘겨주는 값: { id, banner }
  var shown = null;
  var enter = {};
  function route() {
    var v = location.hash.replace('#', '') || 'login';
    if (VIEWS.indexOf(v) < 0) v = 'login';
    VIEWS.forEach(function (name) { $('#view-' + name).hidden = name !== v; });
    sms.hide();
    [signupVerify, findIdVerify, findPwVerify].forEach(function (pv) { pv.stop(); });
    var p = pending || {}; pending = null;
    enter[v](p);
    document.title = TITLES[v] + ' · 기초통신수학 II 문제 은행';
    if (shown !== null && !p.focus) $('#h-' + v).focus();   // 화면이 바뀌면 제목으로 (화면 낭독기용)
    shown = v;
  }
  function go(v, p) {
    pending = p || null;
    history.replaceState(null, '', location.pathname + location.search + '#' + v);
    route();
  }
  $$('[data-go]').forEach(function (btn) {
    btn.addEventListener('click', function () { go(btn.getAttribute('data-go'), { id: btn.dataset.id, focus: true }); });
  });

  /* ── 로그인 ── */
  var liForm = $('#form-login'), liId = $('#li-id'), liPw = $('#li-pw'), liKeep = $('#li-keep');
  var liErr = $('#li-error'), liBanner = $('#login-banner'), liBtn = $('button[type="submit"]', liForm);
  enter.login = function (p) {
    liForm.reset();
    liErr.textContent = '';
    mark(liId, false); mark(liPw, false);
    liPw.type = 'password';
    $('.eye', liForm).setAttribute('aria-pressed', 'false');
    liBanner.hidden = !p.banner;
    liBanner.textContent = p.banner || '';
    if (p.id) liId.value = p.id;
    if (p.focus) (p.id ? liPw : liId).focus();
  };
  function loginFail(input, text) {
    liErr.textContent = text;
    mark(input, true);
    input.focus();
  }
  liForm.addEventListener('submit', function (e) {
    e.preventDefault();
    var id = liId.value.trim().toLowerCase(), pw = liPw.value;
    mark(liId, false); mark(liPw, false); liErr.textContent = '';
    if (!id) return loginFail(liId, '아이디를 입력하세요.');
    if (!pw) return loginFail(liPw, '비밀번호를 입력하세요.');
    var u = users()[id];
    busy(liBtn, true, '확인 중…');
    // 없는 아이디도 같은 시간이 걸리게 해시는 늘 계산
    (u ? checkSecret(u, pw) : derive(pw, randomBytes(16), ITER).then(function () { return false; })).then(function (ok) {
      if (!ok) {
        busy(liBtn, false);
        liPw.value = '';
        mark(liId, true);
        loginFail(liPw, '아이디 또는 비밀번호가 맞지 않아요.');
        return;
      }
      S.start(u.id, liKeep.checked);
      liBtn.textContent = '로그인했어요';
      liBtn.classList.add('is-done');
      announce(u.name + '님, 로그인했어요.');
      $('#auth-face').classList.add('is-open');
      setTimeout(function () { location.replace(next); }, reduceMotion ? 150 : 950);
    }, function () {
      busy(liBtn, false);
      loginFail(liPw, '이 브라우저에서 로그인 확인을 하지 못했어요. 새로고침 후 다시 시도하세요.');
    });
  });

  /* ── 회원가입 ── */
  var su = {
    form: $('#form-signup'), name: $('#su-name'), id: $('#su-id'), pw: $('#su-pw'), pw2: $('#su-pw2'),
    nameMsg: $('#su-name-msg'), idMsg: $('#su-id-msg'), pw2Msg: $('#su-pw2-msg'), rules: $('#su-pw-rules'), err: $('#su-error')
  };
  su.btn = $('button[type="submit"]', su.form);
  var signupVerify = PhoneVerify($('[data-verify="signup"]'), {
    label: '회원가입',
    precheck: function (d) {
      return phoneHash(d).then(function (h) {
        return findByPhone(h) ? '이미 가입한 휴대폰 번호예요. 아이디 찾기에서 아이디를 확인하세요.' : null;
      });
    }
  });
  bindRules(su.pw, su.rules);
  bindConfirm(su.pw, su.pw2, su.pw2Msg);

  function checkSignupId(strict) {
    var v = su.id.value.trim();
    if (!v) {
      setMsg(su.idMsg, strict ? '아이디를 입력하세요.' : ID_HINT, strict ? 'err' : '');
      mark(su.id, strict);
      return false;
    }
    if (!idOk(v)) {
      setMsg(su.idMsg, ID_HINT, strict ? 'err' : '');
      mark(su.id, strict);
      return false;
    }
    if (users()[v]) { setMsg(su.idMsg, '이미 쓰고 있는 아이디예요.', 'err'); mark(su.id, true); return false; }
    setMsg(su.idMsg, '쓸 수 있는 아이디예요.', 'ok');
    mark(su.id, false);
    return true;
  }
  su.id.addEventListener('input', function () { checkSignupId(false); });
  su.id.addEventListener('blur', function () { if (su.id.value) checkSignupId(true); });
  su.name.addEventListener('input', function () { mark(su.name, false); setMsg(su.nameMsg, ''); });
  su.pw.addEventListener('input', function () { mark(su.pw, false); su.err.textContent = ''; });

  enter.signup = function () {
    su.form.reset();
    [su.name, su.id, su.pw, su.pw2].forEach(function (i) { mark(i, false); });
    su.pw.type = 'password';
    $('.eye', su.form).setAttribute('aria-pressed', 'false');
    setMsg(su.nameMsg, ''); setMsg(su.idMsg, ID_HINT); setMsg(su.pw2Msg, '');
    resetRules(su.rules);
    su.err.textContent = '';
    signupVerify.reset();
  };

  su.form.addEventListener('submit', function (e) {
    e.preventDefault();
    su.err.textContent = '';
    var first = null;
    var name = cleanName(su.name.value);
    if (!nameOk(name)) {
      setMsg(su.nameMsg, '이름을 한글이나 영문 2~20자로 입력하세요.', 'err'); mark(su.name, true);
      first = first || su.name;
    }
    if (!checkSignupId(true)) first = first || su.id;
    var r = pwRules(su.pw.value);
    if (!pwOk(su.pw.value)) {
      mark(su.pw, true);
      su.err.textContent = r.space ? '비밀번호에는 공백을 넣을 수 없어요.' : '비밀번호 조건(8~20자, 영문 · 숫자 · 특수문자 중 2가지 이상)을 맞춰 주세요.';
      first = first || su.pw;
    } else mark(su.pw, false);
    if (su.pw2.value !== su.pw.value || !su.pw2.value) {
      setMsg(su.pw2Msg, su.pw2.value ? '비밀번호가 서로 달라요.' : '비밀번호를 한 번 더 입력하세요.', 'err'); mark(su.pw2, true);
      first = first || su.pw2;
    }
    var d = signupVerify.verified();
    if (!d) {
      if (!first) { signupVerify.fail('휴대폰 인증을 마쳐 주세요.'); return; }
      var phoneMsg = $('#su-phone-msg');
      if (!phoneMsg.textContent) setMsg(phoneMsg, '휴대폰 인증을 마쳐 주세요.', 'err');
    }
    if (first) { first.focus(); return; }

    var id = su.id.value.trim();
    busy(su.btn, true, '가입하는 중…');
    Promise.all([makeSecret(su.pw.value), phoneHash(d)]).then(function (res) {
      var secret = res[0], h = res[1];
      var a = S.accounts();
      if (a.users[id]) { busy(su.btn, false); checkSignupId(true); su.id.focus(); return; }
      if (findByPhone(h)) { busy(su.btn, false); signupVerify.reset(); signupVerify.fail('이미 가입한 휴대폰 번호예요. 아이디 찾기에서 아이디를 확인하세요.'); return; }
      a.users[id] = { id: id, name: name, phone: h, phoneMask: maskPhone(d), salt: secret.salt, hash: secret.hash, iter: secret.iter, created: Date.now() };
      S.saveAccounts(a);
      busy(su.btn, false);
      go('login', { id: id, banner: name + '님, 가입을 마쳤어요. 비밀번호를 입력해 로그인하세요.', focus: true });
    }, function () {
      busy(su.btn, false);
      su.err.textContent = '이 브라우저에 계정을 저장하지 못했어요. 저장 공간이 꽉 찼거나 막혀 있는지 확인하세요.';
    });
  });

  /* ── 아이디 찾기 ── */
  var fi = { form: $('#form-find-id'), name: $('#fi-name'), nameMsg: $('#fi-name-msg'), result: $('#fi-result') };
  var fiMatch = null;
  var findIdVerify = PhoneVerify($('[data-verify="find-id"]'), {
    label: '아이디 찾기',
    precheck: function (d) {
      var name = cleanName(fi.name.value);
      if (!nameOk(name)) {
        setMsg(fi.nameMsg, '가입할 때 쓴 이름을 입력하세요.', 'err'); mark(fi.name, true); fi.name.focus();
        return true;
      }
      return phoneHash(d).then(function (h) {
        var u = findByPhone(h);
        if (!u || u.name !== name) return '입력한 이름과 휴대폰 번호로 가입한 아이디가 없어요.';
        fiMatch = u;
        return null;
      });
    },
    onVerified: function () {
      var u = fiMatch;
      fi.form.hidden = true;
      $('#fi-r-name').textContent = u.name;
      $('#fi-r-id').textContent = u.id;
      $('#fi-r-meta').textContent = dateKo(u.created) + ' 가입 · ' + (u.phoneMask || '') + ' 인증';
      $$('[data-go]', fi.result).forEach(function (b) { b.dataset.id = u.id; });
      fi.result.hidden = false;
      announce('아이디는 ' + u.id + '예요.');
    }
  });
  fi.name.addEventListener('input', function () { mark(fi.name, false); setMsg(fi.nameMsg, ''); });
  fi.form.addEventListener('submit', function (e) { e.preventDefault(); });
  enter['find-id'] = function () {
    fi.form.reset(); fi.form.hidden = false; fi.result.hidden = true; fiMatch = null;
    mark(fi.name, false); setMsg(fi.nameMsg, '');
    findIdVerify.reset();
  };

  /* ── 비밀번호 찾기 ── */
  var fp = {
    form: $('#form-find-pw'), id: $('#fp-id'), idMsg: $('#fp-id-msg'), step2: $('#fp-step2'),
    pw: $('#fp-pw'), pw2: $('#fp-pw2'), pw2Msg: $('#fp-pw2-msg'), rules: $('#fp-pw-rules'), err: $('#fp-error')
  };
  fp.btn = $('button[type="submit"]', fp.form);
  var fpUser = null;
  var findPwVerify = PhoneVerify($('[data-verify="find-pw"]'), {
    label: '비밀번호 찾기',
    precheck: function (d) {
      var id = fp.id.value.trim().toLowerCase();
      if (!id) { setMsg(fp.idMsg, '아이디를 입력하세요.', 'err'); mark(fp.id, true); fp.id.focus(); return true; }
      var u = users()[id];
      return phoneHash(d).then(function (h) {
        if (!u || u.phone !== h) return '아이디와 휴대폰 번호가 가입 정보와 맞지 않아요.';
        fpUser = u;
        return null;
      });
    },
    onVerified: function () {
      fp.id.readOnly = true;
      fp.step2.hidden = false;
      fp.pw.focus();
    },
    onReset: function () {
      fp.id.readOnly = false;
      fp.step2.hidden = true;
      fpUser = null;
    }
  });
  bindRules(fp.pw, fp.rules);
  bindConfirm(fp.pw, fp.pw2, fp.pw2Msg);
  fp.id.addEventListener('input', function () { mark(fp.id, false); setMsg(fp.idMsg, ''); });
  [fp.pw, fp.pw2].forEach(function (i) { i.addEventListener('input', function () { mark(fp.pw, false); fp.err.textContent = ''; }); });
  enter['find-pw'] = function (p) {
    fp.form.reset();
    fp.id.readOnly = false;
    fp.step2.hidden = true;
    fpUser = null;
    [fp.id, fp.pw, fp.pw2].forEach(function (i) { mark(i, false); });
    fp.pw.type = 'password';
    $('.eye', fp.form).setAttribute('aria-pressed', 'false');
    setMsg(fp.idMsg, ''); setMsg(fp.pw2Msg, '');
    resetRules(fp.rules);
    fp.err.textContent = '';
    findPwVerify.reset();
    if (p.id) fp.id.value = p.id;
    if (p.focus) (p.id ? $('#fp-phone') : fp.id).focus();
  };
  fp.form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!fpUser || !findPwVerify.verified()) return;
    fp.err.textContent = '';
    var pw = fp.pw.value, r = pwRules(pw);
    if (!pwOk(pw)) {
      mark(fp.pw, true);
      fp.err.textContent = r.space ? '비밀번호에는 공백을 넣을 수 없어요.' : '비밀번호 조건(8~20자, 영문 · 숫자 · 특수문자 중 2가지 이상)을 맞춰 주세요.';
      fp.pw.focus();
      return;
    }
    mark(fp.pw, false);
    if (fp.pw2.value !== pw) {
      setMsg(fp.pw2Msg, fp.pw2.value ? '비밀번호가 서로 달라요.' : '새 비밀번호를 한 번 더 입력하세요.', 'err');
      mark(fp.pw2, true); fp.pw2.focus();
      return;
    }
    busy(fp.btn, true, '바꾸는 중…');
    checkSecret(fpUser, pw).then(function (same) {
      if (same) {
        busy(fp.btn, false);
        mark(fp.pw, true);
        fp.err.textContent = '지금 쓰는 비밀번호와 다른 비밀번호로 정하세요.';
        fp.pw.focus();
        return;
      }
      return makeSecret(pw).then(function (secret) {
        var a = S.accounts(), u = a.users[fpUser.id];
        if (!u) { busy(fp.btn, false); fp.err.textContent = '계정을 찾지 못했어요. 처음부터 다시 시도하세요.'; return; }
        u.salt = secret.salt; u.hash = secret.hash; u.iter = secret.iter; u.changed = Date.now();
        S.saveAccounts(a);
        busy(fp.btn, false);
        go('login', { id: u.id, banner: '비밀번호를 바꿨어요. 새 비밀번호로 로그인하세요.', focus: true });
      });
    }).catch(function () {
      busy(fp.btn, false);
      fp.err.textContent = '이 브라우저에 새 비밀번호를 저장하지 못했어요. 다시 시도하세요.';
    });
  });

  /* ── 시작 ── */
  window.addEventListener('hashchange', route);
  if (params.get('out')) {
    pending = { banner: '로그아웃했어요.' };
    params.delete('out');
    var qs = params.toString();
    history.replaceState(null, '', location.pathname + (qs ? '?' + qs : '') + location.hash);
  }
  route();
  if (shown === 'login' && !liId.value && window.matchMedia && window.matchMedia('(pointer: fine)').matches) liId.focus();
})();
