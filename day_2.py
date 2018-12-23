from aocd import get_data
from aocd import submit
from collections import Counter
import itertools
import re

day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

id_pair = 0
id_triple = 0
lines = data_raw.splitlines()
id_length = len(lines[0])

for line in lines:
    counter = Counter(list(line))

    if 2 in counter.values():
        id_pair += 1

    if 3 in counter.values():
        id_triple += 1

checksum = id_pair * id_triple
print(checksum)

submit(checksum, level=1, day=day, year=2018)

common = ''
for ids in itertools.combinations(lines, 2):
    similarity = sum(map(lambda x: 1 if x[0] == x[1] else 0, zip(*ids)))
    if similarity == id_length - 1:
        common = ''.join(map(lambda x: x[0] if x[0] == x[1] else '', zip(*ids)))
        break

print(common)
submit(common, level=2, day=day, year=2018)
