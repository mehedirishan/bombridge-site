(function () {
  'use strict';

  var CONTACT_EMAIL = 'hello@bombridgegroup.com';

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Problem card accordions
  document.querySelectorAll('.prob-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var body = document.getElementById(btn.getAttribute('aria-controls'));
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      btn.textContent = expanded ? '＋ EXPAND' : '－ COLLAPSE';
      if (body) body.hidden = expanded;
    });
  });

  // Contact form: opens a pre-filled email, nothing is stored or sent from the page
  var form = document.getElementById('connectForm');
  var status = document.getElementById('formStatus');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var v = function (id) { return (document.getElementById(id) || {}).value || ''; };
      var subject = '48-Hour Benchmark Request — ' + (v('f-company') || v('f-name') || 'New enquiry');
      var body = [
        'Name: ' + v('f-name'),
        'Email: ' + v('f-email'),
        'Company: ' + (v('f-company') || '—'),
        'Situation: ' + v('f-stage'),
        '',
        v('f-msg') || '(No additional details provided)',
        '',
        'Requesting the 48-hour zero-risk cost & lead-time benchmark.'
      ].join('\n');
      if (status) status.hidden = false;
      window.location.href = 'mailto:' + CONTACT_EMAIL +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
    });
  }

  // Copy email
  var copyBtn = document.getElementById('copyEmail');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var done = function () {
        copyBtn.textContent = 'COPIED ✓';
        setTimeout(function () { copyBtn.textContent = 'COPY EMAIL'; }, 2200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(CONTACT_EMAIL).then(done, function () {
          copyBtn.textContent = CONTACT_EMAIL;
        });
      } else {
        copyBtn.textContent = CONTACT_EMAIL;
      }
    });
  }
})();
