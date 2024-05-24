document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".add-button");
    const modal = document.getElementById("passkeyModal");
    const closeButton = document.querySelector(".close-button");
    const passkeyInput = document.getElementById("passkeyInput");
    const passkeySubmit = document.getElementById("passkeySubmit");
    let selectedForm = null;

    buttons.forEach(button => {
        button.addEventListener("click", function() {
            selectedForm = document.getElementById(this.dataset.form);
            modal.style.display = "block";
        });
    });

    closeButton.addEventListener("click", function() {
        modal.style.display = "none";
    });

    passkeySubmit.addEventListener("click", function() {
        const passkey = passkeyInput.value;
        // Replace 'your-passkey' with the actual passkey
        if (passkey === 'your-passkey') {
            selectedForm.style.display = "block";
            modal.style.display = "none";
            passkeyInput.value = '';
        } else {
            alert("Clave de acceso incorrecta");
            passkeyInput.value = '';
        }
    });

    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
