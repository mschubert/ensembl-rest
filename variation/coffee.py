import sys, json
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# Get all variants that are associated with the phenotype 'Coffee
# consumption'. For each variant print
# a. the p-value for the association
# b. the PMID for the publication which describes the association between
#    that variant and ‘Coffee consumption’
# c. the risk allele and the associated gene.
#
# Extra: Find the most significant association (lowest p-value) for the
# phenotype 'coffee consumption'

r1 = fetch_endpoint("phenotype/term/human/Coffee consumption")
for r in r1:
    print("{external_reference} {associated_gene} {risk_allele} p={p_value}".format(**r['attributes']))

# Print the allele frequency for the variants’ risk alleles in the Finish
# population. The name of the population is 1000GENOMES:phase_3:FIN

#r2 = fetch_endpoint("info/variation/populations/human") # 13375 populations

ids = {'ids' : [r['Variation'] for r in r1] }

#FIXME: this does not work, but doesn't raise an error either
#  staff created a ticket, so maybe soon?
#ids['pops'] = 1 #"1000GENOMES:phase_3:FIN"


#FIXME: actually look at populations here, something is wrong here

r3 = fetch_endpoint_POST("variation/human?pops=1", data=json.dumps(ids))

for k,v in r3.items():
    print(k, "\tminor: {minor_allele}\tfreq: {MAF}".format(**v))
