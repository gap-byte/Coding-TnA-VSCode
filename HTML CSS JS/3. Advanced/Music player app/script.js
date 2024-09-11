// JavaScript for Custom Music Player Controls
var audio = document.getElementById('audio-element');
var playlistItems = document.querySelectorAll('#playlist li');
var currentTrackIndex = 0; //initialize current track index
var tracks = [
  'HTML%20CSS%20JS/3.%20Advanced/Music%20player%20app/Bruno%20Mars%20-%20Locked%20Out%20Of%20Heaven.mp3',
  'HTML%20CSS%20JS/3.%20Advanced/Music%20player%20app/Linkin%20Park%20-%20In%20The%20End.mp3',
  'HTML%20CSS%20JS/3.%20Advanced/Music%20player%20app/Maroon%205%20-%20Girls%20Like%20You.mp3',
];
n                                                  jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj

function togglePlayPause() {
  if (audio.paused) {
      audio.play();
      updatePlayPauseButton(true);
  } else {
      audio.pause();
      updatePlayPauseButton(false);
  }
}

function updatePlayPauseButton(isPlaying) {
  var playPauseButton = document.getElementById('play-pause');
  playPauseButton.innerText = isPlaying ? 'Pause' : 'Play';
}

function playNextTrack() {
  currentTrackIndex = (currentTrackIndex + 1) % tracks.length;
  changeTrack(tracks[currentTrackIndex], playlistItems[currentTrackIndex]);
}

function playPreviousTrack() {
  currentTrackIndex = (currentTrackIndex - 1 + tracks.length) % tracks.length;
  changeTrack(tracks[currentTrackIndex], playlistItems[currentTrackIndex]);
}

function changeTrack(source, element) {
  audio.src = source;
  audio.play();
  updatePlayPauseButton(true);
  updatePlaylistHighlight(element);
}

function updatePlaylistHighlight(element) {
  if (element) {
      playlistItems.forEach(li => li.classList.remove('playing'));
      element.classList.add('playing');
  }
}

audio.addEventListener('ended', playNextTrack);

audio.addEventListener('timeupdate', function() {
  var progressBar = document.getElementById('progress');
  if (!isNaN(audio.duration)) {
    var percentage = Math.floor((100 / audio.duration) * audio.currentTime);
    progressBar.style.width = percentage + '%';
  }
});

// Error handling for failed audio loading
audio.addEventListener('error', function() {
  alert('Failed to load the audio file.');
});

// Adding click event listeners to playlist items
playlistItems.forEach((item, index) => {
  item.addEventListener('click', function() {
      currentTrackIndex = index;
      changeTrack(tracks[currentTrackIndex], this);
  });
});

// Load the first track on page load
window.onload = function() {
  changeTrack(tracks[0], playlistItems[0]);
};