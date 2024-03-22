document.addEventListener('DOMContentLoaded', function() {
    const profileLink = document.getElementById('access-code');
    profileLink.addEventListener('click', function(event) {
        event.preventDefault();
        
        const accessCodeInputContainer = document.getElementById('access-code-input-container');
        accessCodeInputContainer.style.display = 'block';
    });

    // Select the icon element by class name or any other appropriate selector
    const submitAccessCodeButton = document.querySelector('.fa-arrow-right'); 
    submitAccessCodeButton.addEventListener('click', submitAccessCode);

    const accessCodeInput = document.getElementById('access-code-input');
    accessCodeInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            submitAccessCode();
        }
    });

    async function submitAccessCode() {
        const accessCode = accessCodeInput.value;
        if (accessCode.trim() === '') {
            alert('Error: Debe ingresar un código de acceso.');
            return;
        }
        
        try {
            // Send an asynchronous request to check if the access code exists
            const response = await fetch(`/check-access-code/${accessCode}`);
            const data = await response.json();
            
            if (data.exists) {
                // Access code exists, redirect the user to the agregar_perfil route
                window.location.href = '/agregar_perfil';
            } else {
                // Access code not found, display error message
                alert('Código no encontrado.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Ha ocurrido un error al verificar el código de acceso.');
        }
    }
});
