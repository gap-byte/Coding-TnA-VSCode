// Initialize the map using Leaflet.js
function initMap() {
    // The location of the event
    var eventLocation = [37.4429964, -122.1545229]; // Latitude and Longitude

    // Create the map and set the initial view
    var map = L.map('map').setView(eventLocation, 15);

    // Load and display the OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Add a marker at the event location
    L.marker(eventLocation).addTo(map)
      .bindPopup('TechConf 2024 Location')
      .openPopup();
  }

  // Call initMap when the page loads
  window.onload = initMap;