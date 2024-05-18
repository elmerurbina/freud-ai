document.addEventListener("DOMContentLoaded", function() {
    const codigoForm = document.getElementById("codigo-form");
    const credencialesForm = document.getElementById("credenciales-form");
    const codigoInput = document.getElementById("codigo-input");
    const codigoError = document.getElementById("codigo-error");

    codigoForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const codigo = codigoInput.value.trim();
        
        // Send AJAX request to check código validity
        fetch("/check_code_validity", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ codigo: codigo }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.valid) {
                // Display the credenciales form
                credencialesForm.style.display = "block";
                codigoForm.style.display = "none";
                codigoError.textContent = ""; // Clear any previous error message
            } else {
                // Display error message
                codigoError.textContent = "Código incorrecto, inténtalo de nuevo.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
