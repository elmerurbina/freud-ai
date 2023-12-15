document.querySelector('button[name="Register"]').addEventListener('click', function(event) {
    event.preventDefault(); 

    const form = document.querySelector('.form-group-left');
    const inputs = form.querySelectorAll('input[required]');

    inputs.forEach(input => {
        const span = input.nextElementSibling;

        if (!input.checkValidity()) {
            input.classList.add('invalid');
            const customErrorMessage = input.dataset.customError || 'Este campo es obligatorio';
            span.textContent = customErrorMessage;
            span.style.display = 'block';
            span.style.color = 'yellow';
            span.style.fontSize = '0.8em';
        } else {
            input.classList.remove('invalid');
            span.textContent = '';
            span.style.display = 'none';
        }
    });

    
    if (form.checkValidity()) {
        form.submit();
    }
});









