/* Maison Miette — storefront behaviour */
(function () {
    'use strict';

    /* Format a number as South African Rand: 2500 -> "R2 500" */
    function formatZAR(amount) {
        return 'R' + String(amount).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    }

    /* Build one piece card */
    function renderPiece(p) {
        var soldOut = p.soldOut === true;
        var card = document.createElement('article');
        card.className = 'piece' + (soldOut ? ' is-sold-out' : '') + (p.signature ? ' is-signature' : '');

        var buyBtn = soldOut
            ? '<span class="btn btn-piece is-disabled" aria-disabled="true">Sold out</span>'
            : '<a class="btn btn-piece" href="' + p.url + '" target="_blank" rel="noopener">Buy · ' + formatZAR(p.price) + '</a>';

        card.innerHTML =
            '<figure class="piece-media">' +
                '<img src="' + p.image + '" alt="' + p.name + ' — ' + p.style + '" loading="lazy" ' +
                    'onerror="this.style.display=\'none\';this.closest(\'.piece-media\').classList.add(\'no-image\');">' +
                '<span class="monogram" aria-hidden="true">' + (p.monogram || p.name.charAt(0)) + '</span>' +
                (p.signature ? '<span class="ribbon">Signature piece</span>' : '') +
                (soldOut ? '<span class="sold-tag">Sold out</span>' : '<span class="oneofone-tag">1 of 1</span>') +
            '</figure>' +
            '<div class="piece-body">' +
                '<h3 class="piece-name">' + p.name + '</h3>' +
                '<p class="piece-style">' + p.style + '</p>' +
                '<p class="piece-desc">' + p.description + '</p>' +
                '<div class="piece-foot">' +
                    '<span class="piece-price">' + formatZAR(p.price) + '</span>' +
                    buyBtn +
                '</div>' +
            '</div>';
        return card;
    }

    function renderCollection() {
        var grid = document.getElementById('pieces-grid');
        if (!grid || typeof PRODUCTS === 'undefined') return;
        var frag = document.createDocumentFragment();
        PRODUCTS.forEach(function (p) { frag.appendChild(renderPiece(p)); });
        grid.appendChild(frag);
    }

    /* Mobile navigation toggle */
    function initNav() {
        var burger = document.getElementById('hamburger');
        var menu = document.getElementById('nav-menu');
        if (!burger || !menu) return;
        burger.addEventListener('click', function () {
            var open = menu.classList.toggle('open');
            burger.classList.toggle('open', open);
            burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        menu.addEventListener('click', function (e) {
            if (e.target.classList.contains('nav-link')) {
                menu.classList.remove('open');
                burger.classList.remove('open');
                burger.setAttribute('aria-expanded', 'false');
            }
        });
    }

    /* Contact form — front-end only stub */
    function initForm() {
        var form = document.getElementById('contact-form');
        var note = document.getElementById('form-note');
        if (!form) return;
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            if (!form.checkValidity()) {
                if (note) note.textContent = 'Please complete every field.';
                return;
            }
            form.reset();
            if (note) note.textContent = 'Thank you — your note is on its way. We will reply soon.';
        });
    }

    function init() {
        renderCollection();
        initNav();
        initForm();
        var yr = document.getElementById('year');
        if (yr) yr.textContent = new Date().getFullYear();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
