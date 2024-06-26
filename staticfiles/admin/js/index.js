document.querySelector('.read-more-btn').addEventListener('click', function() {
    // Hide about-images and show mission-card-images
    var aboutImages = document.querySelector('.about-images');
    aboutImages.style.display = 'none';
    
    var missionCardImages = document.querySelector('.mission-card-images');
    missionCardImages.style.display = 'flex';

    // Toggle the visibility of story-card and mission-card
    document.querySelector('.story-card').style.display = 'none';
    document.querySelector('.mission-card').classList.add('fade-in');
    document.querySelector('.mission-card').style.display = 'block';
});