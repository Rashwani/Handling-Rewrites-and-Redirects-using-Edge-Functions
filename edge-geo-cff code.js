function handler(event) {
    //extracting location information from request and creating the redirected response
    var request = event.request;
    var headers = request.headers;
    var host = request.headers.host.value;
    var country = 'US' // Choose a country code
    var newurl = `/cff-geo-en-us.html` // Change the redirect URL to your choice

    if (headers['cloudfront-viewer-country']) {
        var countryCode = headers['cloudfront-viewer-country'].value;
        if (countryCode === country) {
            var response = {
                statusCode: 302,
                statusDescription: 'Found',
                headers:
                    { "location": { "value": newurl } }
                }

            return response;
        }
    }
    return request;
}
