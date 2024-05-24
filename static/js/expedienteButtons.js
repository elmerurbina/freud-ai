document.addEventListener('DOMContentLoaded', () => {
    const addButtons = document.querySelectorAll('.add-button');
    const passkeyModal = document.getElementById('passkeyModal');
    const passkeyInput = document.getElementById('passkeyInput');
    const passkeySubmit = document.getElementById('passkeySubmit');
    const errorMessage = document.getElementById('error-message');
    let currentFormType = '';

    addButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentFormType = button.getAttribute('data-form');
            passkeyModal.style.display = 'block';
        });
    });

    passkeySubmit.addEventListener('click', () => {
        const passkey = passkeyInput.value;
        const formData = new FormData();
        formData.append('passkey', passkey);
        formData.append('form_type', currentFormType);

        fetch('/validate_passkey', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById(currentFormType).style.display = 'block';
                passkeyModal.style.display = 'none';
                passkeyInput.value = '';
                errorMessage.textContent = '';
            } else {
                errorMessage.textContent = 'Clave incorrecta, por favor intentalo nuevamente!';
                errorMessage.style.color = 'red';
                errorMessage.style.fontWeight = 'bold';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'Ocurrio un error, por favor intentalo de nuevo!.';
            errorMessage.style.color = 'red';
            errorMessage.style.fontWeight = 'bold';
        });
    });

    document.querySelector('.close-button').addEventListener('click', () => {
        passkeyModal.style.display = 'none';
        passkeyInput.value = '';
        errorMessage.textContent = '';
    });
});
