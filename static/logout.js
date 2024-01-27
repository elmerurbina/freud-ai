// script.js

document.getElementById('logoutButton').addEventListener('click', function() {
    // Show a confirmation dialog
    var confirmation = confirm('¿Seguro que desea salir?');

    // If the user clicks "OK" (true), close the window/tab
    if (confirmation) {
        window.close();
    }
    // If the user clicks "Cancel" (false), do nothing
});
