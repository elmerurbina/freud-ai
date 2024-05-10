document.addEventListener('DOMContentLoaded', function() {
    // Get all delete profile buttons
    const deleteProfileButtons = document.querySelectorAll('.delete-profile');

    // Add event listener for each delete profile button
    deleteProfileButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default form submission behavior

            const profileId = button.dataset.profileId;

            const confirmDelete = confirm('¿Estás seguro de que deseas eliminar este perfil?');
            if (confirmDelete && profileId) {
                deleteProfile(profileId, button.parentElement.parentElement);
            } else {
                console.log('Delete operation canceled or profile ID not found.');
            }
        });
    });

    // Function to send a POST request to delete the profile
    function deleteProfile(profileId, profileContainer) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', `/delete_profile/${profileId}`);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Remove the deleted profile from the UI
                profileContainer.remove();
                console.log('Perfil eliminado correctamente.');
            } else {
                console.error('Error:', xhr.statusText);
            }
        };
        xhr.onerror = function() {
            console.error('Network Error:', xhr.statusText);
        };
        xhr.send();
    }
});
