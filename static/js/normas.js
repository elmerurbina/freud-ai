document.addEventListener('DOMContentLoaded', function() {
    var accessTermsLink = document.getElementById('norms-terms');

    accessTermsLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action of the link

        // Define styles for the popup window
        var popupStyles = 'width=600,height=600,top=100,left=100,scrollbars=yes';

        // Create a new window for the access terms
        var accessTermsWindow = window.open('', '_blank', popupStyles);

        // Write access terms content to the new window
        accessTermsWindow.document.write('<html><head><title>Términos de Acceso</title>');
        accessTermsWindow.document.write('<style>');
        accessTermsWindow.document.write('body { font-family: Arial, sans-serif; padding: 20px; background: rgba(173, 216, 230, 0.2);}');
        accessTermsWindow.document.write('h2, h3 { margin-bottom: 15px; }');
        accessTermsWindow.document.write('p, ul { margin-bottom: 10px; }');
        accessTermsWindow.document.write('b { font-weight: bold; }');
        accessTermsWindow.document.write('</style>');
        accessTermsWindow.document.write('</head><body>');
        accessTermsWindow.document.write('<h2>Normativa para Psicólogos Certificados</h2>');
        accessTermsWindow.document.write('<p>1. Confidencialidad y Privacidad: Como psicólogo certificado, estás obligado a mantener la confidencialidad de toda la información de los usuarios a los que accedas a través de la plataforma. No debes compartir ni divulgar ningún dato confidencial sin el consentimiento expreso del usuario, a menos que exista una obligación legal que lo requiera.</p>');
        accessTermsWindow.document.write('<p>2. Uso Responsable de la Información: La información de los usuarios solo debe utilizarse con fines terapéuticos y para brindarles el apoyo adecuado. No debes utilizar la información con ningún otro propósito, como fines comerciales o de investigación, sin el consentimiento previo del usuario.</p>');
        accessTermsWindow.document.write('<p>3. Respeto y Empatía: Debes tratar a todos los usuarios con respeto, empatía y comprensión. No debes discriminar ni juzgar a los usuarios por su condición o situación, y debes proporcionarles un ambiente seguro y acogedor para expresarse libremente.</p>');
        accessTermsWindow.document.write('<p>4. Integridad Profesional: Debes ejercer tu práctica profesional de acuerdo con los más altos estándares éticos y profesionales. No debes participar en ninguna actividad que pueda comprometer tu integridad o la confianza de los usuarios en tu capacidad para ayudarles.</p>');
        accessTermsWindow.document.write('<p>5. Notificación de Riesgos: Si identificas algún riesgo de suicidio u otra situación de crisis durante una sesión de terapia, debes tomar medidas inmediatas para garantizar la seguridad del usuario. Esto puede incluir la notificación de emergencia a las autoridades pertinentes o la derivación a servicios de atención médica adecuados.</p>');
        accessTermsWindow.document.write('<p>6. Cumplimiento de la Legislación: Debes cumplir con todas las leyes y regulaciones aplicables relacionadas con la práctica de la psicología y la protección de datos personales. Esto incluye, entre otras cosas, el cumplimiento de la normativa de privacidad y la protección de datos vigente en tu jurisdicción.</p>');
        accessTermsWindow.document.write('<h3>7. Sanciones por Incumplimiento</h3>');
        accessTermsWindow.document.write('<p>8. El incumplimiento de estas normas éticas y profesionales puede resultar en sanciones disciplinarias, que pueden incluir la suspensión o revocación de tu licencia para ejercer la psicología en la plataforma. Se tomarán medidas adicionales si se considera que el incumplimiento ha causado daño o perjuicio a los usuarios.</p>');
        accessTermsWindow.document.write('<h2>9. Otras Reglas</h2>');
        accessTermsWindow.document.write('<ul>');
        accessTermsWindow.document.write('<li>Respetar la confidencialidad de los datos de los usuarios en todo momento.</li>');
        accessTermsWindow.document.write('<li>Brindar atención profesional y ética a todos los usuarios.</li>');
        accessTermsWindow.document.write('<li>Reportar cualquier situación de riesgo para la salud mental de los usuarios de manera inmediata.</li>');
        accessTermsWindow.document.write('<li>No divulgar información personal o confidencial de los usuarios sin su consentimiento explícito.</li>');
        accessTermsWindow.document.write('</ul>');
        accessTermsWindow.document.write('</body></html>');
    });
});
