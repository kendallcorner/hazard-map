var script = document.createElement('script');

SECRET_KEY = 'AIzaSyDjkgyUNU_rBD2v7hVb31aLzB6Gypi1LGw';

script.setAttribute('src','https://maps.googleapis.com/maps/api/js?key='+SECRET_KEY+'&callback=initMap&libraries=places');

document.body.appendChild(script);
