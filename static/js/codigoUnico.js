document.addEventListener("DOMContentLoaded", function() {
    const aseguradoraLink = document.getElementById("aseguradora-link");
    const codigoInput = document.getElementById("codigo-input");

    aseguradoraLink.addEventListener("click", function(event) {
        event.preventDefault();
        codigoInput.style.display = "block";
    });
});
