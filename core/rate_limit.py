import sys
sys.path.append("..")
from helper import fetch_endpoint, fetch_endpoint_POST

#http://rest.ensembl.org/lookup/symbol/human/IRAK4?content-type=application/json

# Write a script to query the ping endpoint 25 times, for each loop
# iteration print the count, the HTTP Status Code, and the
# X-RateLimit-Remaining header.
# Hint: Look at the requests documentation if you’re using Python
# Do you notice anything odd with the count as the whole class is
# running their scripts? What happens to the status code if you
# increase the number of loops to 100?

server = "http://rest.ensembl.org/"

# 200: ok
# 429: too many requests
for i in range(50):
    r = requests.get(server+"info/ping",
            headers={ "Content-Type" : 'application/json'})

    print(i, r.status_code, r.headers['X-RateLimit-Remaining'])
