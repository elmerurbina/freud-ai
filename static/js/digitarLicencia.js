document.addEventListener('DOMContentLoaded', function() {
    const licenseInputContainer = document.getElementById('license-input-container');
    const profileContainer = document.getElementById('profile-container');
    const submitLicenseIcon = document.getElementById('submit-license');

    // Event listener for clicking on the submit icon
    submitLicenseIcon.addEventListener('click', function() {
        const licenseNumber = document.getElementById('license-input').value;
        
        if (licenseNumber.trim() === '') {
            alert('Error: Debe llenar el campo de licencia.');
        } else {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/check_profile');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    if ('error' in response) {
                        alert(response.error);
                    } else {
                        profileContainer.innerHTML = xhr.responseText;
                        licenseInputContainer.style.display = 'none';
                        profileContainer.style.display = 'block'; // Show profile container
                    }
                } else {
                    console.error('Error:', xhr.statusText);
                }
            };
            xhr.onerror = function() {
                console.error('Error:', xhr.statusText);
            };
            xhr.send('licencia=' + encodeURIComponent(licenseNumber));
        }
    });
});
