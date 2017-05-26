import sys
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# A. Write a script to retrieve the gene called IRAK4 (hint: look at the endpoints
# under Lookup) and prints the results
# B. Using this same script, extract and print the Ensembl stable id for this gene
# from the results received from the server

# http://rest.ensembl.org/lookup/symbol/human/IRAK4?content-type=application/json
r1 = fetch_endpoint("lookup/symbol/human/IRAK4")
print(r1['id'])

# Using the script from (b), add a call to fetch and print the sequence for this
# gene in fasta

r2 = fetch_endpoint("sequence/id/" + r1['id'], content_type="text/x-fasta")
print("\n".join(r2.split()[1:4]))

# Print the stable id(s) for all the transcript(s) of this gene (hint, look at the
# ‘expand’ option under /lookup)

r3 = fetch_endpoint("lookup/id/" + r1['id'] + "?expand=1")
print([t['id'] for t in r3['Transcript']])

# Print the start and end for this gene on the GRCh37 assembly (hint: look at
# the Mapping endpoints)

var = {
    'chr' : r1['seq_region_name'],
    'start' : r1['start'],
    'end' : r1['end'],
    'strand' : r1['strand']
}
r4 = fetch_endpoint("map/human/GRCh38/{chr}:{start}..{end}:{strand}/GRCh37".format(**var))

# r1['strand'] is 1, so forward
# seq_region_name is the chromosome
