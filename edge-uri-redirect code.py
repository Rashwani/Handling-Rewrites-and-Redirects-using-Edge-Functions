import json
def lambda_handler(event, context):
    #Let's extract the URI from the request
    get_uri = event['Records'][0]['cf']['request']['uri']
    print(get_uri)
    
    #Let's see what is the uri on the request and redirect it to a different one
    if (get_uri == '/uri-main.html'):
        response = {
            'status': '301',
            'statusDescription': 'Permanent Redirect',
            'headers': {
                'location': [{
                    'key': 'Location',
                    'value': '/uri-redirect.html'
                }]
            }
        }
        #The response above has been created and a response will be sent to the viewer to redirect it to the uri we want them to be served.
        return response
    else:
        #if there is a differnt uri it will move the request as it was made originally
        request = event['Records'][0]['cf']['request']
        return request
