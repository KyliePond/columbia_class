import random

listing = []

for value in range(0, 10000):
    n = random.randint(1,9)
    listing.append(n)
    result = set(listing)
