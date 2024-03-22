document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("support-form");
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting

        // Get form data
        var contactOneInput = document.getElementById("contact-one");
        var contactTwoInput = document.getElementById("contact-two");
        var psychologistEmailInput = document.getElementById("psychologist-email");

        var contactOne = contactOneInput.value;
        var contactTwo = contactTwoInput.value;
        var psychologistEmail = psychologistEmailInput.value;

        // Check if country code is included
        if (!contactOne.includes("+") || !contactTwo.includes("+")) {
            showMessage("Por favor, asegúrese de incluir el código de país en los números de contacto.", "error");
            return;
        }

        // If validation passes, submit the form
        form.submit();
    });

    function showMessage(message, type) {
        var messageElement = document.getElementById("message");
        messageElement.textContent = message;
        messageElement.className = type; // Apply appropriate CSS class for styling
    }
});
