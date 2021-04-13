var script = document.createElement('script');

console.log('SECRET_KEY :>> ', process.env.GCP_KEY);

script.setAttribute('src','https://maps.googleapis.com/maps/api/js?key='+process.env.GCP_KEY+'&callback=initMap&libraries=places');

document.body.appendChild(script);
