document.addEventListener('DOMContentLoaded', function() {
    const licenseInputContainer = document.getElementById('license-input-container');
    const submitLicenseIcon = document.getElementById('submit-license');

    // Event listener for clicking on the submit icon
    submitLicenseIcon.addEventListener('click', function() {
        const licenseNumber = document.getElementById('license-input').value.trim();
        
        if (licenseNumber === '') {
            alert('Error: Debe llenar el campo de licencia.');
        } else {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/check_profile');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = xhr.responseText;
                    // Update the current page with the content returned by the server
                    document.body.innerHTML = response;
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
