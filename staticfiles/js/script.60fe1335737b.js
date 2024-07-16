// JavaScript to toggle the hamburger menu
document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menu-icon');
    const navLinks = document.getElementById('nav-links');

    menuIcon.addEventListener('click', function() {
        navLinks.classList.toggle('show');
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Show the overlay
    var overlay = document.getElementById("coming-soon-overlay");
    overlay.style.display = "flex";
});
