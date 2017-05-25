import sys
sys.path.append(".")
from helper import fetch_endpoint, fetch_endpoint_POST

#http://rest.ensembl.org/lookup/symbol/human/IRAK4?content-type=application/json

server = "http://rest.ensembl.org/"

for i in range(50):
    r = requests.get(server+"info/ping",
            headers={ "Content-Type" : 'application/json'})

    print(i, r.status_code, r.headers['X-RateLimit-Remaining'])
