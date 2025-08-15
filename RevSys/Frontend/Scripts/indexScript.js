// Product Listings JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Product listings page loaded');
    
    // You can add interactive functionality here
    // For example: product card click handlers, dynamic loading, etc.
    
    // Example: Add click handlers to product cards
    const productCards = document.querySelectorAll('.product-card');
    
    productCards.forEach(card => {
        card.addEventListener('click', function() {
            console.log('Product card clicked:', this.querySelector('.product-title').textContent);
            // Add your click handling logic here
        });
        
        // Add hover effects
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// Function to dynamically add products (for Django integration)
function addProduct(title, description, imageUrl = null) {
    const container = document.querySelector('.products-container');
    
    const productCard = document.createElement('div');
    productCard.className = 'product-card';
    
    productCard.innerHTML = `
        <div class="product-image" ${imageUrl ? `style="background-image: url('${imageUrl}'); background-size: cover; background-position: center;"` : ''}></div>
        <div class="product-details">
            <div class="star-rating"></div>
            <h3 class="product-title">${title}</h3>
            <p class="product-description">${description}</p>
        </div>
    `;
    
    container.appendChild(productCard);
    
    // Add event listeners to new card
    productCard.addEventListener('click', function() {
        console.log('Product card clicked:', title);
    });
    
    productCard.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-2px)';
        this.style.transition = 'transform 0.2s ease';
    });
    
    productCard.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
}

// Export for Django use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { addProduct };
}
