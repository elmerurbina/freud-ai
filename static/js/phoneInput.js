var input1 = document.querySelector("#contact-one");
var input2 = document.querySelector("#contact-two");
var input3 = document.querySelector("#psychologist-contact");

var iti1 = window.intlTelInput(input1, {
    separateDialCode: true,
    initialCountry: "ni",
    geoIpLookup: function(success, failure) {
        // Make an AJAX request to get the user's country code
        // and call success(countryCode) or failure() accordingly
    },
});

var iti2 = window.intlTelInput(input2, {
    separateDialCode: true,
    initialCountry: "ni",
    geoIpLookup: function(success, failure) {
        // Make an AJAX request to get the user's country code
        // and call success(countryCode) or failure() accordingly
    },
});

var iti2 = window.intlTelInput(input3, {
    separateDialCode: true,
    initialCountry: "ni",
    geoIpLookup: function(success, failure) {
        // Make an AJAX request to get the user's country code
        // and call success(countryCode) or failure() accordingly
    },
});


