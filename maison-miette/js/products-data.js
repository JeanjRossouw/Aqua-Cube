/*
 * Maison Miette — product catalogue
 * ----------------------------------
 * Edit this file to manage the storefront. Each entry is one one-of-one piece.
 *
 *   price    — number, in South African Rand (ZAR). Shown as e.g. "R2 500".
 *   image    — path to the photo. Drop files into maison-miette/images/products/.
 *              Until a photo exists, the card shows an elegant monogram placeholder.
 *   url      — link the "Buy" button opens (the live Shopify product page).
 *              NOTE: handles below are best-guesses — confirm them in Shopify admin
 *              (Products → a product → "View"/SEO) and adjust if needed.
 *   soldOut  — set to true once the single edition has been sold. The card then
 *              greys out and the button reads "Sold out".
 */
const SHOP_BASE = 'https://yixwg3-3d.myshopify.com';

const PRODUCTS = [
    {
        id: 'aurelie',
        name: 'The Aurélie Bridal Gown',
        style: 'Satin · pearl & crystal sash',
        description: 'Ivory satin bridal gown with a pearl-and-crystal sash, sheer veil and tiara. Hand-sewn.',
        price: 2500,
        monogram: 'A',
        image: 'images/products/aurelie.jpg',
        url: SHOP_BASE + '/products/the-aurelie-bridal-gown',
        soldOut: false
    },
    {
        id: 'rosalind',
        name: 'The Rosalind Gown',
        style: 'Tiered tulle · blush satin',
        description: 'Tiered tulle over blush satin, gathered by hand. The signature piece of the collection.',
        price: 1700,
        monogram: 'R',
        image: 'images/products/rosalind.jpg',
        url: SHOP_BASE + '/products/the-rosalind-gown',
        soldOut: false,
        signature: true
    },
    {
        id: 'capri',
        name: 'The Capri Gown',
        style: 'Pink halter · navy floral skirt',
        description: 'Pink halter bodice over a full navy floral skirt, hand-finished.',
        price: 1450,
        monogram: 'C',
        image: 'images/products/capri.jpg',
        url: SHOP_BASE + '/products/the-capri-gown',
        soldOut: false
    },
    {
        id: 'garden-tea',
        name: 'The Garden Tea Dress',
        style: 'Tiered floral · tulle overlay',
        description: 'Tiered tea dress in garden florals under a soft tulle overlay.',
        price: 1200,
        monogram: 'G',
        image: 'images/products/garden-tea.jpg',
        url: SHOP_BASE + '/products/the-garden-tea-dress',
        soldOut: false
    },
    {
        id: 'brigitte',
        name: 'The Brigitte Set',
        style: 'Denim · lace peplum · two-piece',
        description: 'Washed-denim two-piece: a lace-trimmed peplum top over a matching skirt.',
        price: 1050,
        monogram: 'B',
        image: 'images/products/brigitte.jpg',
        url: SHOP_BASE + '/products/the-brigitte-set',
        soldOut: false
    },
    {
        id: 'heartbeat',
        name: 'The Heartbeat Set',
        style: 'Ribbed knit · for him',
        description: 'A ribbed knit two-piece cut for a boy doll.',
        price: 950,
        monogram: 'H',
        image: 'images/products/heartbeat.jpg',
        url: SHOP_BASE + '/products/the-heartbeat-set',
        soldOut: false
    }
];
