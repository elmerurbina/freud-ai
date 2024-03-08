document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("support-form");
    
    // Function to toggle input field visibility
    function toggleInputVisibility(inputId) {
        const input = document.getElementById(inputId);
        input.style.display = input.style.display === "none" ? "block" : "none";
    }
    
    // Add event listeners to each contact label
    const contactLabels = ["contacto1", "contacto2", "correo del psicologo"];
    contactLabels.forEach(label => {
        const labelElement = document.querySelector(`label[for="${label}"]`);
        labelElement.innerHTML = `Contacto ${label.split("-")[1]}`;
        labelElement.addEventListener("click", function() {
            toggleInputVisibility(label);
        });
    });
    
    // Submit event listener
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        
        // Fetch form data
        const contactOne = document.getElementById("contact-one").value;
        const contactTwo = document.getElementById("contact-two").value;
        const psychologistEmail = document.getElementById("psychologist-email").value;
        
        // Send data to backend
        fetch("/support", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ contactOne, contactTwo, psychologistEmail })
        })
        .then(response => response.json())
        .then(data => {
            // Display success message
            document.getElementById("message").innerHTML = data.message;
        })
        .catch(error => {
            console.error("Error:", error);
            // Display error message
            document.getElementById("message").innerHTML = "Ocurrio un error. Intentalo mas tarde.";
        });
    });
    
    // Search psychologist button click listener
    document.getElementById("search-psychologist").addEventListener("click", function() {
        // Code to search for psychologist
        // You can implement your logic here
    });
    
    // Event listener para agregar más contactos
    document.getElementById("add-contact").addEventListener("click", function() {
        // Obtener el último campo de contacto y su índice
        const lastContact = document.querySelector('div[id^="contact-"]:last-of-type');
        const lastContactIndex = parseInt(lastContact.id.split("-")[1]);
        
        // Crear un nuevo campo de contacto y agregarlo al formulario
        const newContactIndex = lastContactIndex + 1;
        const newContactLabel = document.createElement("label");
        newContactLabel.setAttribute("for", `contact-${newContactIndex}`);
        newContactLabel.innerHTML = `Contacto ${newContactIndex}:`;
        
        const newContactInput = document.createElement("input");
        newContactInput.setAttribute("type", "email");
        newContactInput.setAttribute("id", `contact-${newContactIndex}`);
        newContactInput.setAttribute("name", `contact-${newContactIndex}`);
        newContactInput.setAttribute("placeholder", `Enter contact ${newContactIndex}'s email`);
        
        const newContactDiv = document.createElement("div");
        newContactDiv.appendChild(newContactLabel);
        newContactDiv.appendChild(newContactInput);
        
        // Insertar el nuevo campo antes del botón "Agregar más contactos"
        const addButton = document.getElementById("add-contact");
        addButton.parentNode.insertBefore(newContactDiv, addButton);
        
        // Mostrar el nuevo campo
        toggleInputVisibility(`contact-${newContactIndex}`);
    });
});