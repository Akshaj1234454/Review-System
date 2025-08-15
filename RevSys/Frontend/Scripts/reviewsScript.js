// Review App JavaScript
// This file can be extended with interactive functionality

document.addEventListener('DOMContentLoaded', function() {
    console.log('Review App loaded successfully');
    
    // Example: Add click handler to red placeholder button
    const redPlaceholder = document.querySelector('.red-placeholder');
    if (redPlaceholder) {
        redPlaceholder.addEventListener('click', function() {
            console.log('Red placeholder clicked');
            // Add your functionality here
        });
        
        // Add hover effect
        redPlaceholder.style.cursor = 'pointer';
        redPlaceholder.addEventListener('mouseenter', function() {
            this.style.opacity = '0.8';
        });
        
        redPlaceholder.addEventListener('mouseleave', function() {
            this.style.opacity = '1';
        });
    }
    
    // Example: Add click handler to star rating
    const starRating = document.querySelector('.star-rating');
    if (starRating) {
        starRating.addEventListener('click', function() {
            console.log('Star rating clicked');
            // Add your rating functionality here
        });
        
        starRating.style.cursor = 'pointer';
        starRating.addEventListener('mouseenter', function() {
            this.style.opacity = '0.8';
        });
        
        starRating.addEventListener('mouseleave', function() {
            this.style.opacity = '1';
        });
    }
    
    // Example: Make author name editable on click
    const authorElement = document.querySelector('.author span');
    if (authorElement) {
        authorElement.addEventListener('click', function() {
            const currentText = this.textContent;
            const input = document.createElement('input');
            input.type = 'text';
            input.value = currentText;
            input.style.background = 'transparent';
            input.style.border = '1px solid #fff';
            input.style.color = '#fff';
            input.style.fontFamily = 'Inter, sans-serif';
            input.style.fontSize = window.innerWidth >= 768 ? '32px' : '20px';
            input.style.fontWeight = '400';
            input.style.padding = '4px';
            
            this.parentNode.replaceChild(input, this);
            input.focus();
            
            input.addEventListener('blur', function() {
                const span = document.createElement('span');
                span.textContent = this.value || 'AuthorPlaceHolder';
                span.style.cursor = 'pointer';
                this.parentNode.replaceChild(span, this);
                
                // Re-add click listener to new span
                span.addEventListener('click', arguments.callee);
            });
            
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    this.blur();
                }
            });
        });
        
        authorElement.style.cursor = 'pointer';
        authorElement.title = 'Click to edit';
    }
    
    // Example: Make remarks editable
    const remarksElement = document.querySelector('.remarks span');
    if (remarksElement) {
        remarksElement.addEventListener('click', function() {
            const currentText = this.textContent;
            const textarea = document.createElement('textarea');
            textarea.value = currentText;
            textarea.style.background = 'transparent';
            textarea.style.border = '1px solid #fff';
            textarea.style.color = '#fff';
            textarea.style.fontFamily = 'Inter, sans-serif';
            textarea.style.fontSize = window.innerWidth >= 768 ? '24px' : '16px';
            textarea.style.fontWeight = '400';
            textarea.style.padding = '4px';
            textarea.style.resize = 'vertical';
            textarea.style.minHeight = '100px';
            textarea.style.width = '100%';
            
            this.parentNode.replaceChild(textarea, this);
            textarea.focus();
            
            textarea.addEventListener('blur', function() {
                const span = document.createElement('span');
                span.textContent = this.value || 'Remarks........................';
                span.style.cursor = 'pointer';
                this.parentNode.replaceChild(span, this);
                
                // Re-add click listener to new span
                span.addEventListener('click', arguments.callee);
            });
        });
        
        remarksElement.style.cursor = 'pointer';
        remarksElement.title = 'Click to edit';
    }
});

// Utility functions
function updateLayout() {
    // Function to handle any layout updates on resize
    console.log('Layout updated for viewport:', window.innerWidth);
}

// Add resize listener for responsive adjustments
window.addEventListener('resize', updateLayout);

// Export functions for external use if needed
window.ReviewApp = {
    updateLayout: updateLayout,
    // Add more functions as needed
};
