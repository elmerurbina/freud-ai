document.addEventListener('DOMContentLoaded', function() {
    // Get the support link element
    var supportLink = document.getElementById('support-link');

    // Add click event listener to the support link
    supportLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action of the link

        // Define styles for the popup window
        var popupStyles = 'width=400,height=300,top=100,left=100,scrollbars=yes';

        // Create a new window with contact information
        var contactWindow = window.open('', '_blank', popupStyles);

        // Write contact information to the new window with styles and FontAwesome icons
        contactWindow.document.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">');
        contactWindow.document.write('<style>');
        contactWindow.document.write('body { font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color: #f0f0f0; }'); // Added background color
        contactWindow.document.write('.red-social a { display: block; margin-bottom: 10px; text-align: left; padding-left: 30px; line-height: 30px; text-decoration: none; }'); // Added text-decoration to remove default underline
        contactWindow.document.write('.red-social a:hover { text-decoration: underline; }'); // Underline text on hover
        contactWindow.document.write('.red-social a .fas, .red-social a .fab { margin-right: 10px; }'); // Add space between icon and text
        contactWindow.document.write('</style>');
        contactWindow.document.write('<title>Soporte</title>'); // Add title
        contactWindow.document.write('<h2>Contáctanos</h2>');
        contactWindow.document.write('<div class="red-social">');
        contactWindow.document.write('<a href="mailto:freudiaweb@gmail.com" class="fa fa-envelope">  freudiaweb@gmail.com</a>');
        contactWindow.document.write('<a href="tel:+1234567890" class="fa fa-phone">  +505 5555-0000</a>');
        contactWindow.document.write('<a href="https://t.me/freud_ia" class="fab fa-telegram">  Ir al canal de Telegram</a>');
        contactWindow.document.write('</div>');
    });
});
