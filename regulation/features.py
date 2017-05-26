import sys
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# Areas which influence gene expression are often found
# upstream in close proximity of the gene start.

# Look for regulatory features in the area 1000bp upstream
# of the ESPN gene (Hint: you first need the ENSG ID for
# ESPN).

r1 = fetch_endpoint("lookup/symbol/human/ESPN") # xrefs/symbol for non-HGNC

r1['myend'] = int(r1['start'] - 1000) # leading strand

r2 = fetch_endpoint("overlap/region/human/{seq_region_name}:{myend}..{start}?feature=regulatory".format(**r1))

promotor = r2[0]['ID']

# In which Epigenomes is this feature active?

r3 = fetch_endpoint("regulatory/species/human/id/" + promotor + "?activity=1")

active = [k for k,v in r3[0]['activity'].items() if v == "ACTIVE"]
print(active)

# Look for Motif Features within the Regulatory Feature

# need to go over region here, passing the ENSR id does not work (yet)
#r4 = fetch_endpoint("overlap/id/" + promotor + "?feature=motif")
r4 = fetch_endpoint("overlap/region/human/{seq_region_name}:{start}..{end}?feature=motif".format(**r2[0]))

print("# of binding matrices:", len(r4)

# Look for Variations in each of the Motif Features

variation = dict()
for motif in r4:
    r5 = fetch_endpoint("overlap/region/human/" +
        "{seq_region_name}:{start}..{end}?feature=variation".format(**motif))
    variation[motif['binding_matrix']] = r5
