const audioElement = document.getElementById('audio-element');
const playPauseBtn = document.getElementById('play-pause');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');
const progress = document.getElementById('progress');
const playlist = document.getElementById('playlist');

let isPlaying = false;
let currentTrackIndex = 0;

const tracks = [
    "HTML CSS JS/3. Advanced/Music player app/Bruno Mars - Locked Out Of Heaven.mp3",
    "HTML CSS JS/3. Advanced/Music player app/Linkin Park - In The End.mp3",
    "HTML CSS JS/3. Advanced/Music player app/Maroon 5 - Girls Like You.mp3"
];

function togglePlayPause() {
    if (isPlaying) {
        audioElement.pause();
        playPauseBtn.textContent = 'Play';
    } else {
        audioElement.play();
        playPauseBtn.textContent = 'Pause';
    }
    isPlaying = !isPlaying;
}

function playPreviousTrack() {
    currentTrackIndex--;
    if (currentTrackIndex < 0) {
        currentTrackIndex = tracks.length - 1;
    }
    loadTrack(currentTrackIndex);
}

function playNextTrack() {
    currentTrackIndex++;
    if (currentTrackIndex >= tracks.length) {
        currentTrackIndex = 0;
    }
    loadTrack(currentTrackIndex);
}

function loadTrack(index) {
    audioElement.src = tracks[index];
    audioElement.play();
    isPlaying = true;
    playPauseBtn.textContent = 'Pause';
    updatePlaylistHighlight(index);
}

function changeTrack(src, element) {
    const index = tracks.indexOf(src);
    if (index !== -1) {
        loadTrack(index);
    }
}

function updatePlaylistHighlight(index) {
    const playlistItems = playlist.getElementsByTagName('li');
    for (let i = 0; i < playlistItems.length; i++) {
        playlistItems[i].classList.remove('active');
    }
    playlistItems[index].classList.add('active');
}

audioElement.addEventListener('timeupdate', () => {
    const progressPercent = (audioElement.currentTime / audioElement.duration) * 100;
    progress.style.width = progressPercent + '%';
});

audioElement.addEventListener('ended', () => {
    playNextTrack();
});

playPauseBtn.addEventListener('click', togglePlayPause);
prevBtn.addEventListener('click', playPreviousTrack);
nextBtn.addEventListener('click', playNextTrack);