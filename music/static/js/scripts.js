document.addEventListener('DOMContentLoaded', function() {
    // Handle the shuffle button click event
    const shuffleButton = document.querySelector('.shuffle-button');
    const trackList = document.querySelector('.track-list tbody');
    let tracks = Array.from(trackList.querySelectorAll('tr'));

    // Function to shuffle an array
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    // Function to shuffle tracks
    function shuffleTracks() {
        // Shuffle the tracks array
        const shuffledTracks = shuffleArray(tracks);

        // Clear the current track list
        trackList.innerHTML = '';

        // Append shuffled tracks to the DOM
        shuffledTracks.forEach(function(track) {
            trackList.appendChild(track);
        });
    }

    // Add event listener to the shuffle button
    shuffleButton.addEventListener('click', function() {
        shuffleTracks();
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
