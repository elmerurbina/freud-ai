document.addEventListener("DOMContentLoaded", function() {
    // Conseguir acceso a las variables 
    var feedbackLink = document.getElementById("feedback-link");
    var feedbackForm = document.getElementById("feedback-form");
    var successMessage = document.getElementById("success-message");

   // Funcion del boton enviar
    feedbackForm.addEventListener("submit", function(event) {
        event.preventDefault(); 
        
        successMessage.textContent = "¡Gracias por su opinion!"; // Mensaje a mostrarle al usuario
        successMessage.style.display = "block";

       
        feedbackForm.style.display = "none";

       
        setTimeout(function() {
            successMessage.style.display = "none";
        }, 3000); // Luego de 3 segundos desaparece el mensaje mostrado al usuario
    });


    feedbackLink.addEventListener("click", function(event) {
        event.preventDefault(); 

      
        if (feedbackForm.style.display === "none") {
            feedbackForm.style.display = "block";
            successMessage.style.display = "none"; 
        } else {
            feedbackForm.style.display = "none";
        }
    });
});
