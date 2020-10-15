import random

listing = []

for x in range(0,10000):
    n = random.randint(1,9)
    listing.append(n)

value_ratios = {key: listing.count(key) / len(listing)  for key in listing}


