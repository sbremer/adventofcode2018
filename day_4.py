from aocd import get_data
from aocd import submit
from datetime import datetime
import numpy as np
import re

day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

lines = data_raw.splitlines()

changes = []

for line in lines:
    m = re.match(r'\[(?P<date>.*)\] (?P<data>.*)', line)
    time = datetime.strptime(m.group('date'), '%Y-%m-%d %H:%M')
    data = m.group('data')

    changes.append((time, data))

changes.sort(key=lambda x: x[0])

id = -1
time_sleep = -1
guards = {}
for time, data in changes:

    m = re.match(r'Guard #(?P<id>.*) begins shift', data)
    if m:
        # New guard on duty
        id = int(m.group('id'))
        time_sleep = -1
        if id not in guards:
            guards[id] = np.zeros(60)
    else:
        # Same guard falling asleep and waking up
        if data == 'falls asleep':
            time_sleep = time.minute
        elif data == 'wakes up':
            time_wakeup = time.minute
            guards[id][time_sleep:time_wakeup] += 1.0
        else:
            print('Unknown data: {}'.format(data))

guards_total_sleep = {}
for id in guards:
    total_sleep = np.sum(guards[id])
    guards_total_sleep[id] = total_sleep

id_most_sleep = max(guards_total_sleep.items(), key=lambda x: x[1])[0]

mult = np.argmax(guards[id_most_sleep]) * id_most_sleep

submit(mult, level=1, day=day, year=2018)

min_id = -1
min_asleep = -1
min_asleep_times = -1
for id in guards:

    min_asleep_ = np.argmax(guards[id])
    min_asleep_times_ = np.max(guards[id])
    if min_asleep_times_ > min_asleep_times:
        min_asleep = min_asleep_
        min_asleep_times = min_asleep_times_
        min_id = id

mult2 = min_asleep * min_id

submit(mult2, level=2, day=day, year=2018)
