import sys
import pandas as pd
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# Suppose that you have identified an interesting genomic variant (rs2736340)
# that you would like to investigate further.
# 1. Using the variation endpoint retrieve all information about the variant,
#    including phenotypes, their most severe consequence and traits

variant = "rs2736340"

r1 = fetch_endpoint("variation/human/" + variant + "?phenotypes=1")

print(variant, r1['most_severe_consequence'])
print(list(t['trait'] for t in r1['phenotypes']))

# 2. Find where the variant is located and if it overlaps any regulatory feature.

loc = r1['mappings'][0]['location']
r2 = fetch_endpoint("overlap/region/human/" + loc + "?feature=regulatory")

for r in r2:
    print(r['ID'], r['description'])

# 3. Is the regulatory feature active in any relevant tissues given the
#    phenotypes retrieved?

r3 = fetch_endpoint("regulatory/species/human/id/" + r2[0]['ID'] + "?activity=1")

active = [k for k,v in r3[0]['activity'].items() if v == "ACTIVE"]
print(active)

# To further investigate possible regulatory effects of the variant, we would like to
# query the eQTL data to identify significant associations to any genes.
# 4. List all tissues currently available for eQTL data.

r4 = fetch_endpoint("eqtl/tissue/human")

# 5. Given the phenotypes retrieved above, select the most relevant tissue and
#    then find all genes associated with the genomic variant of interest with a
#    p-value <0.00005 and list their description (xref)

r5 = fetch_endpoint("eqtl/variant_name/human/" + variant + "?statistic=p-value&tissue=Whole_Blood")

df = pd.DataFrame(r5)
print(df.loc[df['value'].astype('float') < 5e-5])
