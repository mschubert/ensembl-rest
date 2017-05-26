import requests

efo_server = "http://www.ebi.ac.uk/"

def efo_request (ext):
    r = requests.get(efo_server+ext,
            headers={ "Content-Type" : "application/json"})

    if not r.ok:
        return

    decoded = r.json()
    return decoded

def fetch_efo(efo_id):
    ext = 'ols/api/ontologies/efo/terms?obo_id=%s' %(efo_id)
    efo_decoded = efo_request(ext)

    if not efo_decoded:
        print("No EFO ID assigned: %s\n"%(efo_id))
        return

    return efo_decoded

def print_efo (efo):
    print("Link(URL): %s" %(efo['_links']['self']['href']))
    for t in efo['_embedded']['terms']:
        print("Link(IRI): %s" %(t['iri']))
        if t['description']:
            for d in t['description']:
                print("Description: %s" %(d))
        else:
            print('No description provided')
    print()
