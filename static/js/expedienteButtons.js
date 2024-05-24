document.addEventListener('DOMContentLoaded', function() {
    // Get the modal and the passkey input field
    var modal = document.getElementById('passkeyModal');
    var passkeyInput = document.getElementById('passkeyInput');
    var passkeySubmit = document.getElementById('passkeySubmit');
    var errorMessage = document.getElementById('error-message');

    // Get all the add buttons
    var addButtons = document.querySelectorAll('.add-button');

    // Attach event listener to each add button
    addButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Show the passkey modal
            modal.dataset.form = button.dataset.form;
            modal.style.display = 'block';
        });
    });

    // When the user clicks on the close button, close the modal
    var closeButton = document.querySelector('.close-button');
    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
        errorMessage.textContent = '';
    });

    // When the user clicks outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
            errorMessage.textContent = '';
        }
    };

    // Add event listener for passkey submission
    passkeySubmit.addEventListener('click', function() {
        var passkey = passkeyInput.value;
        var formType = modal.dataset.form;
        // Make a request to the server to validate the passkey
        fetch('/validate_passkey', {
            method: 'POST',
            body: JSON.stringify({ passkey: passkey, form_type: formType }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        
        .then(response => {
            if (response.status === 200) { // Check if response status is OK
                // Passkey is correct, display the form associated with the button
                var form = document.getElementById(formType);
                modal.style.display = 'none';
                form.style.display = 'block';
            } else {
                // Passkey is incorrect, display an error message
                errorMessage.textContent = 'Clave de acceso incorrecta. Inténtalo de nuevo.';
                errorMessage.style.color = 'red';
                errorMessage.style.fontWeight = 'bold';
            }
        })
        
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
