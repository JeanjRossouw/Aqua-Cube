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
