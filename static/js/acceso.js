// JavaScript (access_terms.js)
document.addEventListener('DOMContentLoaded', function() {
    var accessTermsLink = document.getElementById('access-terms');

    accessTermsLink.addEventListener('click', function(event) {
        event.preventDefault();

        // Define styles for the popup window
        var popupStyles = 'width=600,height=400,top=100,left=100,scrollbars=yes';

        // Create a new window for displaying access terms
        var termsWindow = window.open('', '_blank', popupStyles);

        // Write access terms content to the new window
        termsWindow.document.write('<style>body { font-family: Arial, sans-serif; background-color: #f0f0f0; }</style>');
        termsWindow.document.write('<h2>Términos de Acceso</h2>');
        termsWindow.document.write('<p>1. Acceso Limitado: El acceso a los registros de los usuarios estará disponible únicamente en situaciones críticas, como el riesgo de suicidio. Este acceso se concede con el único propósito de brindar apoyo y atención inmediata al paciente.</p>');
        termsWindow.document.write('<p>2. Confidencialidad: Todos los datos del usuario accesibles para el psicólogo son estrictamente confidenciales. El psicólogo se compromete a mantener la privacidad y confidencialidad de la información del usuario en todo momento.</p>');
        termsWindow.document.write('<p>3. Uso Responsable: El psicólogo utilizará la información del usuario únicamente con el propósito de brindar tratamiento y apoyo psicológico. No se permitirá el uso indebido o la divulgación no autorizada de la información del usuario.</p>');
        termsWindow.document.write('<p>4. Consentimiento Informado: El psicólogo reconoce que el acceso a los mensajes del usuario requiere el consentimiento informado del paciente o su representante legal, según corresponda. Se debe obtener un consentimiento explícito antes de acceder a los registros del usuario.</p>');
        termsWindow.document.write('<p>Al hacer clic en el botón "Acceder", usted acepta cumplir con estos términos y condiciones para acceder a los registros del usuario.</p>');
    });
});
