document.addEventListener('DOMContentLoaded', function() {
    const profileLink = document.getElementById('profile-link');
    profileLink.addEventListener('click', function(event) {
        event.preventDefault(); 
       
        const licenseInputContainer = document.getElementById('license-input-container');
        licenseInputContainer.style.display = 'block';
    });

    
    const submitLicenseButton = document.getElementById('submit-license');
    submitLicenseButton.addEventListener('click', function() {
        // Conseguir los valores del input
        const licenseNumber = document.getElementById('license-input').value;
        
        // Revisar si el input esta vacio
        if (licenseNumber.trim() === '') {
            // Si esta vacio muetsra un mensaje de error
            alert('Error: Debe llenar el campo de licencia.');
        } else {
            // Si la licencia es valida proceder 
            console.log('License Number:', licenseNumber);
        }
    });
});
