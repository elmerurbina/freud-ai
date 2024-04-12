
document.addEventListener('DOMContentLoaded', function() {
    const deleteProfileButton = document.getElementById('delete-profile');

    // Event listener for clicking on the delete profile button
    deleteProfileButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const profileId = deleteProfileButton.dataset.profileId;

        const confirmDelete = confirm('¿Estás seguro de que deseas eliminar este perfil?');
        if (confirmDelete && profileId) {
            deleteProfile(profileId);
        } else {
            console.log('Delete operation canceled or profile ID not found.');
        }
    });

    // Function to send a POST request to delete the profile
    function deleteProfile(profileId) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', `/delete_profile/${profileId}`);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Reload the page after successful deletion
                window.location.reload();
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
