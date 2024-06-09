import json
def lambda_handler(event, context):
    #Let's first get the Country Code from the Request coming in
    get_country_viewer_header = event['Records'][0]['cf']['request']['headers']['cloudfront-viewer-country']
    define_country = get_country_viewer_header[0]['value']
    #Now let's define which country that is and create our redirected response
    if (define_country == 'US'):
        response = {
            'status': '301',
            'statusDescription': 'Permanent Redirect',
            'headers': {
                'location': [{
                    'key': 'Location',
                    'value': '/en-us.html'
                }]
            }
        }
        #The response above has been created and a response will be sent to the viewer to redirect it to the /en-us.html
        return response
    else:
        #if the country has not been identified then move on with the request
        request = event['Records'][0]['cf']['request']
        return request
