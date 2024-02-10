document.getElementById('privacyLink').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default action of the link

    // Define styles for the popup window
    var popupStyles = 'width=600,height=600,top=100,left=100,scrollbars=yes';

    // Create a new window for the privacy terms
    var privacyWindow = window.open('', '_blank', popupStyles);

    // Write privacy terms content to the new window
    privacyWindow.document.write('<html><head><title>Términos de Privacidad</title>');
    privacyWindow.document.write('<style>');
    privacyWindow.document.write('body { font-family: Arial, sans-serif; padding: 20px; background-color: #f0f0f0;}');
    privacyWindow.document.write('h3 { margin-bottom: 15px; }');
    privacyWindow.document.write('p { margin-bottom: 10px; }');
    privacyWindow.document.write('b { font-weight: bold; }');
    privacyWindow.document.write('</style>');
    privacyWindow.document.write('</head><body>');
    privacyWindow.document.write('<div class="privacy-content">');
    privacyWindow.document.write('<h3>Términos de Privacidad</h3>');
    privacyWindow.document.write('<p><b>Confidencialidad de la Información:</b> Garantizamos la confidencialidad de toda la información proporcionada en Freud.AI. Los datos del usuario, las interacciones y la información del expediente están protegidos con medidas de seguridad avanzadas.</p>');
    privacyWindow.document.write('<p><b>Uso de la Información:</b> La información recopilada se utiliza exclusivamente con el propósito de proporcionar servicios psicológicos personalizados. No compartiremos ni venderemos datos a terceros sin el consentimiento explícito del usuario.</p>');
    privacyWindow.document.write('<p><b>Seguridad de Datos:</b> Implementamos medidas de seguridad tecnológicas y organizativas para proteger la integridad y confidencialidad de los datos. Nuestra plataforma cumple con los estándares de seguridad de la industria.</p>');
    privacyWindow.document.write('<p><b>Acceso Limitado:</b> El acceso a la información del expediente está estrictamente limitado a los profesionales autorizados. Se utiliza un sistema de autenticación seguro para garantizar que solo los usuarios autorizados puedan acceder a la información confidencial.</p>');
    privacyWindow.document.write('<p><b>Consentimiento Informado:</b> Antes de utilizar nuestros servicios, solicitamos el consentimiento informado del usuario. Esto incluye la comprensión de cómo se utilizará la información y el compromiso de seguir las políticas de privacidad establecidas.</p>');
    privacyWindow.document.write('<p><b>Registro y Autenticación:</b> El proceso de registro e inicio de sesión está diseñado con altos estándares de seguridad para proteger la identidad del usuario. Se recomienda mantener la información de inicio de sesión de manera segura y confidencial.</p>');
    privacyWindow.document.write('<p><b>Retención de Datos:</b> Mantenemos los datos del usuario durante el tiempo necesario para cumplir con los objetivos establecidos. Se brinda la opción de eliminar la cuenta y los datos personales en cualquier momento.</p>');
    privacyWindow.document.write('<p><b>Actualizaciones de Privacidad:</b> Nos comprometemos a informar a los usuarios sobre cualquier cambio en nuestras políticas de privacidad. Las actualizaciones se comunicarán de manera clara y transparente.</p>');
    privacyWindow.document.write('</div>');
    privacyWindow.document.write('</body></html>');

    // Close the privacy window when the main window is closed
    window.addEventListener('beforeunload', function () {
        privacyWindow.close();
    });
});
