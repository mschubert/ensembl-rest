import sys, json
import pandas as pd
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

# Compute LD in the region 3:196064297-196068186 for the population
# 1000GENOMES:phase_3:CEU. Print all results with r2=1 and
# d_prime=1

r1 = fetch_endpoint("ld/human/region/3:196064297-196068186/1000GENOMES:phase_3:CEU")
df = pd.DataFrame(r1)
print(df.loc[(df['d_prime'].astype('float') == 1) & (df['r2'].astype('float') == 1)])

# Compute pairwise LD for all variants that are not further away from
# rs535797132 than 500kb. Print all variants that are in LD (d_prime >=
# 0.8) with rs535797132. For each pair of variants also print d_prime
# and r2. Use 1000GENOMES:phase_3:FIN as the population

r2 = fetch_endpoint("/ld/human/rs535797132/1000GENOMES:phase_3:FIN")
df = pd.DataFrame(r2)
print(df.loc[(df['d_prime'].astype('float') >= 0.8)])
