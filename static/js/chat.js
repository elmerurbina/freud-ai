// JavaScript code for handling chat functionality

function sendMessage() {
    const userInput = document.getElementById('messageInput').value;
    const messageContainer = document.getElementById('messageContainer');

    // Show the user message
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.innerHTML = `<i class="fa-solid fa-user"></i> ${userInput}`;
    messageContainer.appendChild(userMessage);

    // Scroll to the bottom after sending the message
    messageContainer.scrollTop = messageContainer.scrollHeight;

    // Send the message to the server for processing
    fetch('/process_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Show the chatbot message
        const chatbotMessage = document.createElement('div');
        chatbotMessage.className = 'chatbot-message';
        chatbotMessage.innerHTML = `<i class="fa-brands fa-fly"></i> ${data.response}`;
        messageContainer.appendChild(chatbotMessage);

        // Scroll to the bottom after showing the message
        messageContainer.scrollTop = messageContainer.scrollHeight;

        // Clear the input field after sending the message
        document.getElementById('messageInput').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
        // Clear the input field in case of error
        document.getElementById('messageInput').value = '';
    });
}