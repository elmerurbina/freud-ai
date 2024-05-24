// editarProfesional.js

document.addEventListener('DOMContentLoaded', function() {
    var editProfileButton = document.getElementById('edit-profile-button');
    var editProfileForm = document.getElementById('edit-profile-form');

    if (editProfileButton && editProfileForm) {
        editProfileButton.addEventListener('click', function() {
            populateFormWithExistingInfo();
        });
    }

    function populateFormWithExistingInfo() {
        // Retrieve the existing information
        var nombre = document.getElementById('nombre-profile').innerText;
        var direccion = document.getElementById('direccion-profile').innerText;
        var keywords = document.getElementById('keywords-profile').innerText;
        var contacto = document.getElementById('contacto-profile').innerText;
        var descripcion = document.getElementById('descripcion-profile').innerText;
        var ubicacion = document.getElementById('ubicacion-profile').innerText;
        var estudios_academicos = document.getElementById('estudios_academicos-profile').innerText;
        var whatsapp = document.getElementById('whatsapp-profile').innerText;

        // Populate the form fields with the existing information
        document.getElementById('nombre').value = nombre;
        document.getElementById('direccion').value = direccion;
        document.getElementById('keywords').value = keywords;
        document.getElementById('contacto').value = contacto;
        document.getElementById('descripcion').value = descripcion;
        document.getElementById('ubicacion').value = ubicacion;
        document.getElementById('estudios_academicos').value = estudios_academicos;
        document.getElementById('whatsapp').value = whatsapp;

        // Show the edit profile form
        editProfileForm.style.display = 'block';
    }
});
