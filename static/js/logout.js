// Assuming you have a button with the id "logoutButton"
document.getElementById('logoutButton').addEventListener('click', function() {
    // Show a confirmation dialog
    var confirmation = confirm('¿Seguro que desea salir?');

    // If the user clicks "OK" (true), redirect to index.html
    if (confirmation) {
        window.location.href = "{{ url_for('home') }}";
    }
    // If the user clicks "Cancel" (false), do nothing
});
