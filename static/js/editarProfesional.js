document.getElementById('edit-profile-button').addEventListener('click', function() {
    console.log("Button clicked"); 
    // Show the edit profile form
    document.getElementById('edit-profile-form').style.display = 'block';

    // Populate form fields with existing profile data
    document.getElementById('nombre').value = "{{ profesional.nombre }}";
    document.getElementById('direccion').value = "{{ profesional.direccion }}";
    document.getElementById('keywords').value = "{{ profesional.keywords }}";
    document.getElementById('contacto').value = "{{ profesional.contacto }}";
    document.getElementById('descripcion').value = "{{ profesional.descripcion }}";
    document.getElementById('whatsapp').value = "{{ profesional.whatsapp }}";
});
