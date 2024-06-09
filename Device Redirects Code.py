import json
def lambda_handler(event, context):
    print(event)
    #Let's first get the Device Type from the Request coming in
    get_device_viewer_header = event['Records'][0]['cf']['request']['headers']['cloudfront-is-mobile-viewer']
    define_device_type = get_device_viewer_header[0]['value']
    print(define_device_type)
    #Now let's see if this device is a mobile viewer or not and create the redirected response based on that
    if (define_device_type == 'true'):
        response = {
            'status': '301',
            'statusDescription': 'Permanent Redirect',
            'headers': {
                'location': [{
                    'key': 'Location',
                    'value': '/mobile.html'
                }]
            }
        }
        #The response above has been created and a response will be sent to the viewer to redirect it the right device page
        return response
    else:
        #if the device is not mobile, then move along with the request as is.
        request = event['Records'][0]['cf']['request']
        return request
