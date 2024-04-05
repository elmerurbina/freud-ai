document.querySelector('button[name="Register"]').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent default form submission behavior
    
    const form = document.getElementById('register'); // Adjust the selector for the form
    const fields = form.querySelectorAll('.field'); // Select all fields within the form

    fields.forEach(field => {
        const input = field.querySelector('input[required]');
        const span = field.querySelector('.error');

        if (!input.checkValidity()) {
            input.classList.add('invalid');
            const customErrorMessage = input.dataset.customError || 'Este campo es obligatorio*';
            span.textContent = customErrorMessage;
            span.style.display = 'block';
            span.style.color = 'yellow';
            span.style.fontSize = '0.8em';
            input.style.marginBottom = '5px';
        } else {
            input.classList.remove('invalid');
            span.textContent = '';
            span.style.display = 'none';
        }
    });

    const emailInput = form.querySelector('input[type="email"]');
    if (!isValidEmail(emailInput.value)) {
        showError(emailInput, 'Email no válido');
    }

    const passwordInput = form.querySelector('input[type="password"]');
    if (!isValidPassword(passwordInput.value)) {
        showError(passwordInput, 'Contraseña debe tener al menos 8 caracteres, letras y números');
    }

    const repeatPasswordInput = form.querySelector('input[name="repeat_password"]');
    if (passwordInput.value !== repeatPasswordInput.value) {
        showError(repeatPasswordInput, 'Las contraseñas no coinciden');
    }

    const usernameInput = form.querySelector('input[name="user"]'); // Update the selector for username
    if (!isValidUsername(usernameInput.value)) {
        showError(usernameInput, 'Usuario debe contener solo minúsculas');
    }

    const dobInput = form.querySelector('input[name="date"]');
    const dobValue = dobInput.value.split('-').reverse().join('-'); // Adjust date format
    if (!isValidDateOfBirth(dobValue)) {
        showError(dobInput, 'Debes tener al menos 10 años de edad');
    }

    if (form.checkValidity()) {
        form.submit(); // Submit the form if all validations pass
    }
});

function showError(input, message) {
    const span = input.nextElementSibling;
    input.classList.add('invalid');
    span.textContent = message;
    span.style.display = 'block';
    span.style.color = 'yellow';
    span.style.fontSize = '0.8em';
    input.style.marginBottom = '5px';
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPassword(password) {
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordRegex.test(password);
}

function isValidUsername(username) {
    const usernameRegex = /^[a-z]+$/; // Only lowercase letters allowed
    return usernameRegex.test(username);
}

function isValidDateOfBirth(dob) {
    const today = new Date();
    const birthDate = new Date(dob);
    const age = today.getFullYear() - birthDate.getFullYear();

    return age >= 10; // Ensure the user is at least 10 years old
}