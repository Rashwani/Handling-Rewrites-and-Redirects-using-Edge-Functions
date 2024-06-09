import json
def lambda_handler(event, context):
    #let's first extract the URI from the request
    get_uri = event['Records'][0]['cf']['request']['uri']
    #let's check what is the URI and decide if the URI sent to the Origin should be modified
    if (get_uri == '/uri-rewrite.html'):
        event['Records'][0]['cf']['request']['uri'] = '/rewrite.html'
        request = event['Records'][0]['cf']['request']
        return request
    #if the uri should not be modified then just continue with the request as is
    else:
        request = event['Records'][0]['cf']['request']
        return request
