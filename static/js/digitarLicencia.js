document.addEventListener('DOMContentLoaded', function() {
    const profileLink = document.getElementById('profile-link');
    profileLink.addEventListener('click', function(event) {
        event.preventDefault(); 
        // Mostrar el input que permita escribir el numero de licencia
        const licenseInputContainer = document.getElementById('license-input-container');
        licenseInputContainer.style.display = 'block';
    });

    // 
    const submitLicenseButton = document.getElementById('submit-license');
    submitLicenseButton.addEventListener('click', function() {
        
        const licenseNumber = document.getElementById('license-input').value;
        
        
        console.log('License Number:', licenseNumber);
    });
});
