function sendMessage() {
    const userInput = document.getElementById('messageInput').value;
    const messageContainer = document.getElementById('messageContainer');

    // Mostrar el mensaje
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.innerHTML = `<i class="fa-solid fa-user"></i> ${userInput}`;
    messageContainer.appendChild(userMessage);

    // Desplazarse a la parte inferior despues de enviar el mensaje
    messageContainer.scrollTop = messageContainer.scrollHeight;

    // Enviar el mensaje al servidor para que este lo procese
    fetch('/process_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar el mensaje del chatbot
        const chatbotMessage = document.createElement('div');
        chatbotMessage.className = 'chatbot-message';
        chatbotMessage.innerHTML = `
        <div class="logo-image">
        <img src="static/imagenes/logo.jpg" alt="Logo Image">
        </div>
        <div class="message-text">
            ${data.response}
        </div>
    `;
        messageContainer.appendChild(chatbotMessage);

        // Mover a la parte inferior de la pagina despues de mostrar el mensaje
        messageContainer.scrollTop = messageContainer.scrollHeight;

        // Limpiar el input de los mensajes
        document.getElementById('messageInput').value = '';
    })
    .catch(error => console.error('Error:', error));
}
