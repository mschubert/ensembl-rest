import requests

server =  "http://rest.ensembl.org/"
ct = "application/json"

def fetch_endpoint(request, server=server, content_type=ct):
    """
    Fetch an endpoint using POST, allow overriding of default content-type
    """
    r = requests.get(server+request, headers={ "Content-Type" : content_type})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text

def fetch_endpoint_POST(request, data, server=server, content_type=ct):
    """
    Fetch an endpoint using POST, allow overriding of default content-type
    """
    r = requests.post(server+request, headers={ "Content-Type" : content_type}, data=data )

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text
