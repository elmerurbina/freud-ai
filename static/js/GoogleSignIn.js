// google_signin.js

function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
     // Send the id_token to your backend for authentication
     fetch('/google_login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'id_token': id_token
        })
    })

   .then(function(response) {
        // Handle the response from the backend
        if (response.ok) {
            window.location.href = "{{ url_for('chat') }}";  // Redirect to chat interface using url_for
        }
    }).catch(function(error) {
        console.error('Error:', error);
    });
}
