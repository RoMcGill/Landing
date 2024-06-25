let images = [
    {src: '{% static "images/orange.png" %}', class: 'bg-orange'},
    {src: '{% static "images/blue.png" %}', class: 'bg-blue'},
    {src: '{% static "images/purp.png" %}', class: 'bg-purple'}
];
let index = 0;

function changeImage() {
    let imageElement = document.getElementById('image');
    let ctaButtons = document.querySelectorAll('.cta-button');

    // Update the image source
    imageElement.src = images[index].src;

    // Update classes for buttons
    ctaButtons.forEach(button => {
        button.classList.remove('bg-orange', 'bg-purple', 'bg-blue');
        button.classList.add(images[index].class);
    });

    // Move to the next image
    index = (index + 1) % images.length;
}

// Change image every 4 seconds
setInterval(changeImage, 4000);

// Initial call to set the first image
changeImage();
