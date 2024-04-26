document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const profileCards = document.querySelectorAll('.profile-card');

    searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.toLowerCase();

        profileCards.forEach(card => {
            const keywords = card.getAttribute('data-keywords').toLowerCase();

            if (keywords.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});
