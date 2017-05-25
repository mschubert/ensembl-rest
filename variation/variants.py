import sys, json
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# Print all variants that are located on chromosome 17 between
# 80348215 and 80348333. Use the overlap endpoint to get the location
# (seq_region_name, start, end), alleles, consequence_type and
# clinical_significance for each variant in the region.

r1 = fetch_endpoint("overlap/region/human/7:150990..151014?feature=variation")
ids = {'ids' : [r['id'] for r in r1]}
print(ids)

# Get the variant class, evidence attributes, source and the
# most_severe_consequence for all variants in that region from the
# variant endpoint. Send the variant ids as post request.

r2 = fetch_endpoint_POST("variation/human", data=json.dumps(ids))
for k,v in r2.items():
    print(k, v['var_class'], v['evidence'], v['most_severe_consequence'])

# For each protein coding transcript for the gene ENSG00000145354
# print the number of overlapping variants.

r3 = fetch_endpoint("lookup/id/ENSG00000145354") #?expand=1
region = "{seq_region_name}:{start}..{end}".format(**r3)
r4 = fetch_endpoint("overlap/region/human/7:150990..151014?feature=variation")
ids2 = [r['id'] for r in r4]
print(set(ids['ids']) & set(ids2))
