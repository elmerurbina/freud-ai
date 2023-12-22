document.querySelector('button[name="Register"]').addEventListener('click', function(event) {
    event.preventDefault(); 

    const form = document.querySelector('.form-group-left');
    const inputs = form.querySelectorAll('input[required]');
    const emailInput = form.querySelector('input[type="email"]');
    const passwordInput = form.querySelector('input[type="password"]');
    const repeatPasswordInput = form.querySelector('input[name="repeat_password"]');

    inputs.forEach(input => {
        const span = input.nextElementSibling;

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

   
    if (!isValidEmail(emailInput.value)) {
        showError(emailInput, 'Email no válido');
    }

   
    if (!isValidPassword(passwordInput.value)) {
        showError(passwordInput, 'Contraseña debe tener al menos 8 caracteres, letras y números');
    }

    
    if (passwordInput.value !== repeatPasswordInput.value) {
        showError(repeatPasswordInput, 'Las contraseñas no coinciden');
    }

    if (form.checkValidity()) {
        form.submit();
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

