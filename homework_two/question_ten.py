import random

listing = []

for value in range(0, 10000):
    n = random.randint(0,10)
    listing.append(n)
    listing.sort()
    result = listing[0]

