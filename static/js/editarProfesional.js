document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the edit profile button
    document.getElementById('edit-profile-button').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission
        console.log("Button clicked");

        // Show the edit profile form
        document.getElementById('edit-profile-form').style.display = 'block';

        // Populate form fields with existing profile data (you can load this data via AJAX if needed)
        document.getElementById('nombre').value = "{{ profesional.nombre }}";
        document.getElementById('direccion').value = "{{ profesional.direccion }}";
        document.getElementById('keywords').value = "{{ profesional.keywords }}";
        document.getElementById('contacto').value = "{{ profesional.contacto }}";
        document.getElementById('descripcion').value = "{{ profesional.descripcion }}";
        document.getElementById('whatsapp').value = "{{ profesional.whatsapp }}";
    });

    // Add event listener to the edit profile form submission
    document.getElementById('edit-profile-form-data').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get the form data
        const formData = new FormData(this);

        // Make an AJAX request to update the profile data
        fetch('/edit_profile', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Handle response data (if needed)
            console.log(data);
            // For example, display a success message or handle errors
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
