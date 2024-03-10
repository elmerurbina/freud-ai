document.addEventListener('DOMContentLoaded', function() {
    const profileLink = document.getElementById('access-code');
    profileLink.addEventListener('click', function(event) {
        event.preventDefault();
        
        const accessCodeInputContainer = document.getElementById('access-code-input-container');
        accessCodeInputContainer.style.display = 'block';
    });

    const submitAccessCodeButton = document.getElementById('submit-access-code');
    submitAccessCodeButton.addEventListener('click', function() {
        const accessCode = document.getElementById('access-code-input').value;
        if (accessCode.trim() === '') {
            alert('Error: Debe ingresar un código de acceso.');
        } else {
            // Proceed with your logic, e.g., redirect the user to the desired route
            console.log('Access Code:', accessCode);
        }
    });
});
