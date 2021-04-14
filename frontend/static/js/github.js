var script = document.createElement('script');

SECRET_KEY = 'secret';

script.setAttribute('src','https://maps.googleapis.com/maps/api/js?key='+SECRET_KEY+'&callback=initMap&libraries=places');

document.body.appendChild(script);
