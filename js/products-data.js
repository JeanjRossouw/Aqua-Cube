const products = [
    {
        category: 'Aquariums',
        items: [
            {
                name: '100 Gallon Aquarium',
                description: 'A large aquarium suitable for various fish.',
                price: 299.99,
                imageUrl: 'https://source.unsplash.com/featured/?aquarium'
            },
            {
                name: 'Nano Aquarium',
                description: 'A compact aquarium perfect for small spaces.',
                price: 59.99,
                imageUrl: 'https://source.unsplash.com/featured/?nano-aquarium'
            }
        ]
    },
    {
        category: 'Filters',
        items: [
            {
                name: 'UV Filter',
                description: 'A filter that uses UV light to eliminate harmful bacteria.',
                price: 89.99,
                imageUrl: 'https://source.unsplash.com/featured/?filter'
            },
            {
                name: 'Canister Filter',
                description: 'A powerful external filter for larger aquariums.',
                price: 129.99,
                imageUrl: 'https://source.unsplash.com/featured/?canister-filter'
            }
        ]
    },
    {
        category: 'Lighting',
        items: [
            {
                name: 'LED Aquarium Light',
                description: 'Energy-efficient lighting solution for your aquarium.',
                price: 49.99,
                imageUrl: 'https://source.unsplash.com/featured/?aquarium-light'
            }
        ]
    },
    {
        category: 'Heaters',
        items: [
            {
                name: 'Submersible Heater',
                description: 'Keeps the water temperature stable.',
                price: 34.99,
                imageUrl: 'https://source.unsplash.com/featured/?heater'
            }
        ]
    },
    {
        category: 'Decorations',
        items: [
            {
                name: 'Coral Decoration',
                description: 'Add a touch of the ocean to your aquarium.',
                price: 29.99,
                imageUrl: 'https://source.unsplash.com/featured/?decor'
            }
        ]
    },
    {
        category: 'Air Pumps',
        items: [
            {
                name: 'Quiet Air Pump',
                description: 'Operates silently to aerate your aquarium.',
                price: 39.99,
                imageUrl: 'https://source.unsplash.com/featured/?air-pump'
            }
        ]
    },
    {
        category: 'Food',
        items: [
            {
                name: 'Tropical Fish Food',
                description: 'Nutritionally balanced food for tropical fish.',
                price: 19.99,
                imageUrl: 'https://source.unsplash.com/featured/?fish-food'
            }
        ]
    },
    {
        category: 'Testing',
        items: [
            {
                name: 'Water Test Kit',
                description: 'Test the quality of your aquarium water.',
                price: 24.99,
                imageUrl: 'https://source.unsplash.com/featured/?water-test'
            }
        ]
    },
    {
        category: 'Plants',
        items: [
            {
                name: 'Live Aquarium Plants',
                description: 'Enhance the beauty and health of your aquarium.',
                price: 15.99,
                imageUrl: 'https://source.unsplash.com/featured/?live-plants'
            }
        ]
    },
    {
        category: 'Substrate',
        items: [
            {
                name: 'Aquarium Gravel',
                description: 'Natural gravel for aquarium use.',
                price: 9.99,
                imageUrl: 'https://source.unsplash.com/featured/?substrate'
            }
        ]
    },
    {
        category: 'Paludarium',
        items: [
            {
                name: 'Paludarium Kit',
                description: 'An all-in-one kit for creating a paludarium.',
                price: 179.99,
                imageUrl: 'https://source.unsplash.com/featured/?paludarium'
            }
        ]
    }
];

// Functions to search, filter, sort, and retrieve products
function searchProducts(query) {
    return products.flatMap(category => 
        category.items.filter(item => item.name.toLowerCase().includes(query.toLowerCase()))
    );
}

function filterProductsByCategory(categoryName) {
    const category = products.find(cat => cat.category.toLowerCase() === categoryName.toLowerCase());
    return category ? category.items : [];
}

function sortProductsByPrice(order = 'asc') {
    return products.flatMap(category => category.items).sort((a, b) => 
        order === 'asc' ? a.price - b.price : b.price - a.price
    );
}

function getAllProducts() {
    return products.flatMap(category => category.items);
}

// Example usage:
console.log(searchProducts('aquarium'));
console.log(filterProductsByCategory('Food'));
console.log(sortProductsByPrice('desc'));
console.log(getAllProducts());
