// google_signin.js

function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;

   then(function(response) {
        // Handle the response from the backend
        if (response.ok) {
            window.location.href = "{{ url_for('chat') }}";  // Redirect to chat interface using url_for
        }
    }).catch(function(error) {
        console.error('Error:', error);
    });
}
