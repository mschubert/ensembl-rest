import sys, json
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# Print VEP results for rs189863975
# a. For each overlapping transcript (transcript_consequences) print
#    variant_allele, transcript_id, the consequence_terms and if
#    available the polyphen_score and polyphen_prediction

r1 = fetch_endpoint("vep/human/id/rs189863975")

affected = r1[0]['transcript_consequences']

for a in affected:
    b = {'polyphen_score':'', 'polyphen_prediction':''}
    b.update(a)

    print("{variant_allele} {transcript_id} {consequence_terms} {polyphen_score} {polyphen_prediction}".format(**b))

# Print VEP results for all variants that are located in region
# 19:11400000-11400500. Use the overlap endpoint first to retrieve all
# variants in the specified region and then use the VEP POST id
# endpoint to compute consequences for a list of variants

r2 = fetch_endpoint("overlap/region/human/19:11400000-11400500?feature=variation")
ids = {'ids' : [r['id'] for r in r1]}

r3 = fetch_endpoint_POST("vep/human/id", data=json.dumps(ids))
affected = { r['id'] : r['transcript_consequences'] for r in r3 }

for rsid, a in affected.items():
    for elm in a:
        elm['rsid'] = rsid
        if 'polyphen_score' in elm.keys():
            print("{gene_symbol} {rsid} {polyphen_score} {polyphen_prediction}".format(**elm))
