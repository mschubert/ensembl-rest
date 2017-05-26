import sys
sys.path.append("..")
sys.path.append(".")
from helper import fetch_endpoint, fetch_endpoint_POST
from efo_helper import fetch_efo, print_efo

# links to EFO terms have not yet been mapped in current release
ep = "http://test.rest.ensembl.org/"

# List all Epigenomes available in Ensembl Regulation

r1 = fetch_endpoint("regulatory/species/human/epigenome", server=ep)
print(r1[0:2])

# Find additional information (where available) for each
# epigenome using the Ontology Lookup Service

efo_ids = [t['efo_id'] for t in r1 if t['efo_id'] != None]
efo = [fetch_efo(e) for e in efo_ids]

print_efo(efo[0])
print_efo(efo[1])
