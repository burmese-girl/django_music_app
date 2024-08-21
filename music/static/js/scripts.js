document.addEventListener('DOMContentLoaded', function() {
    // Handle the shuffle button click event
    const shuffleButton = document.querySelector('.shuffle-button');
    shuffleButton.addEventListener('click', function() {
        alert('Shuffle button clicked! Shuffle functionality can be added here.');
    });

    // Handle play/pause button click event in the player
    const playPauseButton = document.querySelector('#play-pause-button');
    const audioPlayer = document.querySelector('#current-track-player');

    playPauseButton.addEventListener('click', function() {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playPauseButton.textContent = 'Pause';
        } else {
            audioPlayer.pause();
            playPauseButton.textContent = 'Play';
        }
    });

    // Additional functionality can be added here, such as loading the next track, etc.
});
