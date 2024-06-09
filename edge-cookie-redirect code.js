function handler(event)  { 
    console.log('code is starting')
    var request = event.request;
    var cookie_exists = request.cookies
    //evaluates if a request has a cookie, if it does not immediately redirects the viewer to the login page
    if (cookie_exists.session == null) {
        console.log("start if block")
        var response = {
            statusCode: 301,
            statusDescription: 'Permanent Redirect',
            headers:
                { "location": { "value": "/login.html" } }
            }
        return response;
    //in case the first condition is false, it means we have a cookie, we need to know now if the cookie we need is set to the value we need.
    } else if (cookie_exists.session.value != "true") {
        console.log("start else if block")
        var response = {
            statusCode: 301,
            statusDescription: 'Permanent Redirect',
            headers:
                { "location": { "value": "/login.html" } }
            }
        return response;
    // if none of the above conditions are met it means the cookie is set, then we just allow the request to proceed as is
    } else {
    return request;
    }
}
