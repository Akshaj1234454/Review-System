// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get form elements
    const form = document.getElementById('signupForm');
    const fullNameInput = document.getElementById('fullName');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const actionBtn1 = document.getElementById('actionBtn1');
    const actionBtn2 = document.getElementById('actionBtn2');

    // Form validation function
    function validateForm() {
        const fullName = fullNameInput.value.trim();
        const email = emailInput.value.trim();
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;

        // Basic validation
        if (!fullName) {
            showError(fullNameInput, 'Full name is required');
            return false;
        }

        if (!email || !isValidEmail(email)) {
            showError(emailInput, 'Valid email is required');
            return false;
        }

        if (!password || password.length < 6) {
            showError(passwordInput, 'Password must be at least 6 characters');
            return false;
        }

        if (password !== confirmPassword) {
            showError(confirmPasswordInput, 'Passwords do not match');
            return false;
        }

        return true;
    }

    // Email validation helper
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Show error function
    function showError(input, message) {
        // Remove existing error
        clearError(input);

        // Add error styling
        input.style.borderColor = '#ef4444';
        input.style.backgroundColor = '#fef2f2';

        // Create error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        errorDiv.style.color = '#ef4444';
        errorDiv.style.fontSize = '0.875rem';
        errorDiv.style.marginTop = '0.25rem';

        // Insert error message
        input.parentNode.appendChild(errorDiv);

        // Focus the input
        input.focus();
    }

    // Clear error function
    function clearError(input) {
        input.style.borderColor = '';
        input.style.backgroundColor = '#d4d4d8';

        const errorMessage = input.parentNode.querySelector('.error-message');
        if (errorMessage) {
            errorMessage.remove();
        }
    }

    // Clear errors on input
    [fullNameInput, emailInput, passwordInput, confirmPasswordInput].forEach(input => {
        input.addEventListener('input', function() {
            clearError(this);
        });
    });


    // Handle form submission: validate, then allow normal submit if valid
    form.addEventListener('submit', function(e) {
        if (!validateForm()) {
            e.preventDefault(); // Only prevent if invalid
        }
    });

    // Handle cancel/reset (action button 2)
    actionBtn2.addEventListener('click', function() {
        // Clear form and errors
        form.reset();
        [fullNameInput, emailInput, passwordInput, confirmPasswordInput].forEach(input => {
            clearError(input);
        });

        console.log('Form reset');
    });



    // Add keyboard navigation for action buttons
    actionBtn1.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            this.click();
        }
    });

    actionBtn2.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            this.click();
        }
    });

    // Password strength indicator (optional enhancement)
    passwordInput.addEventListener('input', function() {
        const password = this.value;
        const strength = calculatePasswordStrength(password);
        updatePasswordStrength(strength);
    });

    function calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 6) strength++;
        if (password.length >= 10) strength++;
        if (/[a-z]/.test(password)) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[^A-Za-z0-9]/.test(password)) strength++;
        return strength;
    }

    function updatePasswordStrength(strength) {
        // Remove existing strength indicator
        const existingIndicator = passwordInput.parentNode.querySelector('.password-strength');
        if (existingIndicator) {
            existingIndicator.remove();
        }

        if (passwordInput.value.length > 0) {
            const strengthDiv = document.createElement('div');
            strengthDiv.className = 'password-strength';
            strengthDiv.style.marginTop = '0.25rem';
            strengthDiv.style.fontSize = '0.75rem';

            if (strength < 3) {
                strengthDiv.textContent = 'Weak password';
                strengthDiv.style.color = '#ef4444';
            } else if (strength < 5) {
                strengthDiv.textContent = 'Medium password';
                strengthDiv.style.color = '#f59e0b';
            } else {
                strengthDiv.textContent = 'Strong password';
                strengthDiv.style.color = '#10b981';
            }

            passwordInput.parentNode.appendChild(strengthDiv);
        }
    }
});
