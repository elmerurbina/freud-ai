// notification.js

// JavaScript function to display custom notification modal
function displayConfirmationMessage(event) {
    event.preventDefault(); // Prevent form submission

    // Check if at least one category is selected
    var selectedCategories = document.querySelectorAll('input[name="category"]:checked');
    var timeInterval = document.querySelector('input[name="time"]:checked');

    if (selectedCategories.length === 0 || !timeInterval) {
        alert("Debe seleccionar al menos una opción y un intervalo de tiempo.");
        return;
    }

    // Show the notification modal
    var modal = document.getElementById('notificationModal');
    modal.style.display = 'block';

    // Hide the modal after 3 seconds (adjust as needed)
    setTimeout(function() {
        modal.style.display = 'none';
    }, 3000);
}

// JavaScript function to close the notification modal
function closeNotificationModal() {
    var modal = document.getElementById('notificationModal');
    modal.style.display = 'none';
}
