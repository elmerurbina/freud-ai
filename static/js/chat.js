
function sendMessage() {
    const userInput = document.getElementById('messageInput').value;
    const messageContainer = document.getElementById('messageContainer');

    // Display user message
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.innerHTML = `<i class="fa-solid fa-user"></i> ${userInput}`;
    messageContainer.appendChild(userMessage);

    // Scroll to the bottom of the message container
    messageContainer.scrollTop = messageContainer.scrollHeight;

    // Send user message to the server for processing
    fetch('/process_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot response
        const chatbotMessage = document.createElement('div');
        chatbotMessage.className = 'chatbot-message';
        chatbotMessage.innerHTML = `<i class="fa-brands fa-fly"></i> ${data.response}`;
        messageContainer.appendChild(chatbotMessage);

        // Scroll to the bottom of the message container
        messageContainer.scrollTop = messageContainer.scrollHeight;

        // Clear input field
        document.getElementById('messageInput').value = '';
    })
    .catch(error => console.error('Error:', error));
}





/*
function sendMessage() {
    const userInput = document.getElementById('messageInput').value;
    const messageContainer = document.getElementById('messageContainer');

    // Display user message
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.innerHTML = `<i class="fa-solid fa-user"></i> ${userInput}`;
    messageContainer.appendChild(userMessage);

    // Send user message to the server for processing
    fetch('/process_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot response
        const chatbotMessage = document.createElement('div');
        chatbotMessage.className = 'chatbot-message';
        chatbotMessage.innerHTML = `<i class="fa-solid fa-brain"></i> ${data.response}`;
        messageContainer.appendChild(chatbotMessage);

        // Clear input field
        document.getElementById('messageInput').value = '';
    })
    .catch(error => console.error('Error:', error));
}
*/