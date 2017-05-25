import sys
sys.path.append(".")
from helper import fetch_endpoint, fetch_endpoint_POST

#http://rest.ensembl.org/lookup/symbol/human/IRAK4?content-type=application/json

r1 = fetch_endpoint("lookup/symbol/human/IRAK4")
print(r1['id'])

r2 = fetch_endpoint("sequence/id/" + r1['id'], content_type="text/x-fasta")
print("\n".join(r2.split()[1:4]))

r3 = fetch_endpoint("lookup/id/" + r1['id'] + "?expand=1")
print([t['id'] for t in r3['Transcript']])

# r1['strand'] is 1, so forward
# seq_region_name is the chromosome
var = {
    'chr' : r1['seq_region_name'],
    'start' : r1['start'],
    'end' : r1['end'],
    'strand' : r1['strand']
}
r4 = fetch_endpoint("map/human/GRCh38/{chr}:{start}..{end}:{strand}/GRCh37".format(**var))
