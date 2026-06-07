/* Maison Miette — theme.js (progressive enhancement only) */
(function () {
  'use strict';

  /* Mobile navigation */
  function initNav() {
    var toggle = document.querySelector('[data-nav-toggle]');
    var nav = document.querySelector('[data-site-nav]');
    if (!toggle || !nav) return;
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* Collection filter chips — client-side filter by data-categories */
  function initFilters() {
    var chipBar = document.querySelector('[data-filter-chips]');
    var grid = document.querySelector('[data-filter-grid]');
    if (!chipBar || !grid) return;
    var cards = Array.prototype.slice.call(grid.querySelectorAll('[data-categories]'));
    var empty = document.querySelector('[data-filter-empty]');

    chipBar.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip');
      if (!chip) return;
      var value = chip.getAttribute('data-filter');
      chipBar.querySelectorAll('.chip').forEach(function (c) { c.classList.toggle('is-active', c === chip); });

      var shown = 0;
      cards.forEach(function (card) {
        var cats = (card.getAttribute('data-categories') || '').split(',');
        var match = value === '*' || cats.indexOf(value) !== -1;
        card.style.display = match ? '' : 'none';
        if (match) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  }

  /* Product gallery — thumbnail switches the main image */
  function initGallery() {
    var gallery = document.querySelector('[data-gallery]');
    if (!gallery) return;
    var main = gallery.querySelector('[data-gallery-main]');
    var thumbs = gallery.querySelectorAll('[data-gallery-thumb]');
    if (!main || !thumbs.length) return;
    thumbs.forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        var src = thumb.getAttribute('data-src');
        var alt = thumb.getAttribute('data-alt') || '';
        if (src) { main.src = src; main.alt = alt; }
        thumbs.forEach(function (t) { t.classList.toggle('is-active', t === thumb); });
      });
    });
  }

  function ready(fn) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn);
    else fn();
  }
  ready(function () { initNav(); initFilters(); initGallery(); });
})();
