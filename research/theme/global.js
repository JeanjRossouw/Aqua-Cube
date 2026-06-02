// Mobile hamburger toggle
(function () {
  const hamburger = document.getElementById('Hamburger');
  const menu = document.getElementById('NavMenu');
  if (hamburger && menu) {
    hamburger.addEventListener('click', function () {
      const open = menu.classList.toggle('active');
      hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  const mq = window.matchMedia('(max-width: 720px)');

  // Mobile dropdown accordions: tap a category to expand/collapse its panel
  document.querySelectorAll('.ac-nav__drop > .ac-nav__trigger').forEach(function (trigger) {
    trigger.addEventListener('click', function (e) {
      if (!mq.matches) return; // desktop keeps hover behaviour
      e.preventDefault();
      const drop = trigger.closest('.ac-nav__drop');
      const willOpen = !drop.classList.contains('is-open');
      document.querySelectorAll('.ac-nav__drop.is-open').forEach(function (d) {
        if (d !== drop) { d.classList.remove('is-open'); }
      });
      drop.classList.toggle('is-open', willOpen);
      trigger.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
      if (!willOpen) { trigger.blur(); } // release :focus-within so it actually closes
    });
  });

  // Dismiss the mobile menu after tapping a real link
  if (menu) {
    menu.querySelectorAll('a[href]').forEach(function (link) {
      link.addEventListener('click', function () {
        if (mq.matches) { menu.classList.remove('active'); }
      });
    });
  }

  // PDP: thumbnail swap
  const mainImage = document.getElementById('ProductImage');
  if (mainImage) {
    document.querySelectorAll('.product-thumb').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const src = btn.getAttribute('data-src');
        if (src) mainImage.src = src;
      });
    });
  }
})();
