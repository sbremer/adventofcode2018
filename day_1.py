from aocd import get_data
from aocd import submit
import itertools
import re

day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

freq = 0
for expression in data_raw.splitlines():
    freq += int(expression)

print(freq)
submit(freq, level=1, day=day, year=2018)

freq = 0
freqs = {}
for expression in itertools.cycle(data_raw.splitlines()):
    freq += int(expression)
    if freq in freqs:
        break
    else:
        freqs[freq] = 1

print(freq)
submit(freq, level=2, day=day, year=2018)
