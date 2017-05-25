import sys
import requests
import json
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

#http://rest.ensembl.org/lookup/symbol/human/IRAK4?content-type=application/json

# Fetch IRAK4 using the expand option

r1 = fetch_endpoint("lookup/symbol/human/IRAK4")
print(r1['id'])

# Fetch the sequences for all the transcripts using a single
# POST request, print the transcript sequences in fasta
# format

r2 = fetch_endpoint("lookup/id/" + r1['id'] + "?expand=1")

transcripts = {'ids' : [t['id'] for t in r2['Transcript']]}

r3 = fetch_endpoint_POST("sequence/id",
        data = json.dumps(transcripts),
        content_type="text/x-fasta")
