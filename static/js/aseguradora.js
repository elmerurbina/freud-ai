document.addEventListener("DOMContentLoaded", function() {
    const codigoForm = document.getElementById("codigo-form");
    const credencialesForm = document.getElementById("credenciales-form");
    const codigoInput = document.getElementById("codigo-input");
    const codigoError = document.getElementById("codigo-error");

    codigoForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const codigo = codigoInput.value.trim();
        // Simulate AJAX request to check if the código ejecutivo exists
        if (codigo === "codigo_valido") {
            // Display the credenciales form
            credencialesForm.style.display = "block";
            codigoForm.style.display = "none";
        } else {
            // Display error message
            codigoError.textContent = "Código incorrecto, inténtalo de nuevo.";
        }
    });
});
