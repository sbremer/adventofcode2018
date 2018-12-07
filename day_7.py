from aocd import get_data
from aocd import submit
from collections import defaultdict
from copy import deepcopy
import re

day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

# Step D must be finished before step L can begin.
# (first_step, following_step)
data = [(re.findall("Step (.*?) must", line)[0],
         re.findall("step (.*?) can", line)[0])
        for line in data_raw.splitlines()]

steps = set()
needs = defaultdict(set)
enables = defaultdict(set)
for (dependent, step) in data:
    needs[step].add(dependent)
    enables[dependent].add(step)
    steps.add(dependent)
    steps.add(step)
    # print('{} before {}'.format(dependent, step))

needs_unedited = deepcopy(needs)

sequence = ''
while True:
    possible_steps = [step for step in steps if len(needs[step]) == 0]
    if len(possible_steps) == 0:
        break

    next_step = min(possible_steps)
    sequence += next_step
    needs[next_step].add('_')

    for step in enables[next_step]:
        needs[step].remove(next_step)

print(sequence)
submit(sequence, level=1, day=day, year=2018)

# Level 2
needs = needs_unedited


def get_time(step):
    return 60 + ord(step) - 64


workers_max = 5
workers = dict()
ts = 0
while True:
    for step, t in list(workers.items()):
        if t <= ts:
            for fstep in enables[step]:
                needs[fstep].remove(step)

            del workers[step]

    possible_steps = [step for step in steps if len(needs[step]) == 0]

    if len(possible_steps) == 0 and len(workers) == 0:
        break

    while len(possible_steps) > 0 and len(workers) < workers_max:
        next_step = min(possible_steps)
        possible_steps.remove(next_step)
        sequence += next_step
        needs[next_step].add('_')
        workers[next_step] = ts + get_time(next_step)

    ts = min(workers.values())

print(ts)
submit(ts, level=2, day=day, year=2018)
