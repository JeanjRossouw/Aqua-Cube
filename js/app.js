// Sample products array
const products = [
    { id: 1, name: 'Aquarium Kit', price: 59.99, featured: true },
    { id: 2, name: 'Fish Food', price: 12.99, featured: true },
    { id: 3, name: 'Aquarium Filter', price: 29.99, featured: false },
    { id: 4, name: 'Decorative Plants', price: 15.49, featured: false },
    { id: 5, name: 'Aquarium Heater', price: 45.00, featured: true },
    { id: 6, name: 'Aquarium Gravel', price: 10.00, featured: true }
];

let cart = [];

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push({ ...product, quantity: 1 });
        updateCartCount();
    }
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateCartCount();
}

function updateQuantity(productId, quantity) {
    const item = cart.find(item => item.id === productId);
    if (item) {
        item.quantity = quantity;
        if (item.quantity <= 0) {
            removeFromCart(productId);
        }
    }
}

function displayCart() {
    console.log('Shopping Cart:', cart);
}

function displayFeaturedProducts() {
    const featured = products.filter(product => product.featured);
    console.log('Featured Products:', featured);
}

function displayAllProducts() {
    console.log('All Products:', products);
}

function displayCartSummary() {
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    console.log('Cart Summary: Total Amount - $' + total.toFixed(2));
}

function checkout() {
    if (cart.length === 0) {
        console.log('No items in cart.');
        return;
    }
    displayCartSummary();
    cart = [];
    updateCartCount();
    console.log('Checkout completed.');
}

function updateCartCount() {
    const count = cart.reduce((sum, item) => sum + item.quantity, 0);
    console.log('Cart count updated: ' + count);
}