import random

listing = []

for x in range(0,10000):
    n = random.randint(1,9)
    listing.append(n)

value_counts = {key: listing.count(key) for key in listing}



        
