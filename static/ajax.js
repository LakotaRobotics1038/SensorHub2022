// HTTP request

var request = new XMLHttpRequest();

// Listener for completed requests
request.onload = () => {
	if (request.status >= 200 && request.status < 300) {
		console.log('success', request);
	} else {
		console.log('request failed');
	}

	console.log('running');
} 

// send request

var url = 'http://' + document.domain + ':' + location.port + '/request-test';

request.open('GET', url);

request.send();
