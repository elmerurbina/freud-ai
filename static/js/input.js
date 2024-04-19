function sendMessage() {
    var messageInput = document.getElementById('messageInput');
    var messageText = messageInput.value;

    if (messageText.trim() !== '') {
        appendUserMessage(messageText);
        simulateBotReply();
        messageInput.value = '';
    }
}

function appendUserMessage(text) {
    var messageContainer = document.getElementById('messageContainer');
    var newMessage = document.createElement('div');
    newMessage.className = 'user-message';
    newMessage.innerText = text;
    messageContainer.appendChild(newMessage);
}

function simulateBotReply() {
    var messageContainer = document.getElementById('messageContainer');
    var newMessage = document.createElement('div');
    newMessage.className = 'bot-message';
    newMessage.innerText = '¡Gracias por tu mensaje! Estoy procesando la información...';
    messageContainer.appendChild(newMessage);

    // Simulate a delayed response
    setTimeout(function () {
        newMessage.innerText = 'Aquí tienes una respuesta simulada del bot. ¡Espero que sea útil!';
        // Scroll to the bottom to show the latest message
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }, 2000);
}