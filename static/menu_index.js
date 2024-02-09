document.addEventListener('DOMContentLoaded', function() {
    // Get the "More Options" toggle element
    var moreOptionsToggle = document.querySelector('.more-options-toggle');
    var moreOptionsMenu = document.querySelector('.more-options-menu');

    // Add click event listener to the "More Options" toggle
    moreOptionsToggle.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action of the link
        event.stopPropagation(); // Prevent the event from bubbling up to the document body

        // Toggle the visibility of the additional options menu
        moreOptionsMenu.classList.toggle('active');
    });

    // Add click event listener to the document body to close the menu when clicking anywhere on the page
    document.body.addEventListener('click', function(event) {
        // Check if the clicked element is not within the "More Options" block
        if (!moreOptionsMenu.contains(event.target) && !moreOptionsToggle.contains(event.target)) {
            // Close the menu by removing the 'active' class
            moreOptionsMenu.classList.remove('active');
        }
    });
});
