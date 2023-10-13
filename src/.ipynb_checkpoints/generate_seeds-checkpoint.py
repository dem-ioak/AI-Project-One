import json
import numpy.random as random

seeds = dict()

for i in range(100):
    seeds[i] = random.randint(1,10**16)

SEEDS_FILE_PATH = 'src/seeds.txt'
with open(SEEDS_FILE_PATH, 'w') as seeds_file:
    seeds_file.write(json.dumps(seeds))
