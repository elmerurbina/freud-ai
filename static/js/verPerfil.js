// Informacion del perfil
const profile = {
  
    license: '12F345',
    nombre: 'John Doe',
    direccion: 'Chontales, Nicaragua',
    descripcion: 'Profesional de psicologia certificado',
    keywords: ['ansiedad', 'covid_19', 'ansiedad_medicamentos'],
    contacto: 'john@example.com',
    estudios_academicos: 'Licenciado en psicologia, UNAN-Leon'
};

// Funcion para mostrar los datos
function displayProfile() {
    
    document.getElementById('license').textContent = profile.license;
    document.getElementById('nombre').textContent = profile.nombre;
    document.getElementById('direccion').textContent = profile.direccion;
    document.getElementById('descripcion').textContent = profile.descripcion;
    document.getElementById('keywords').textContent = profile.keywords.join(', ');
    document.getElementById('contacto').textContent = profile.contacto;
    document.getElementById('estudios').textContent = profile.estudios_academicos;
}

// Llamar la funcion para mostrar los datos una vez cargue la pagina 
window.onload = displayProfile;
