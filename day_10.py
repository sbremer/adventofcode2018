from aocd import get_data
import re
import numpy as np

day = 10
data_raw = get_data(day=day)
lines = data_raw.splitlines()


def display_message(pos):
    min = np.min(pos, 0)
    max = np.max(pos, 0)

    size = max - min + 1

    display = [[' ' for _ in range(size[0])] for _ in range(size[1])]
    pos -= min

    for point in pos:
        display[point[1]][point[0]] = '#'

    for line in display:
        print(''.join(line))


N = len(lines)

pos = np.zeros((N, 2)).astype(int)
vel = np.zeros((N, 2)).astype(int)

for at, line in enumerate(lines):
    m = re.match(r'position=<(?P<pos_x>.*),(?P<pos_y>.*)> velocity=<(?P<vel_x>.*),(?P<vel_y>.*)>', line)
    pos_ = int(m.group('pos_x')), int(m.group('pos_y'))
    vel_ = int(m.group('vel_x')), int(m.group('vel_y'))

    pos[at, :] = pos_
    vel[at, :] = vel_

norm_last = float('inf')
seconds = 0
while True:
    pos += vel
    seconds += 1
    norm = np.linalg.norm(pos - np.mean(pos, 0))

    if norm > norm_last:
        break
    norm_last = norm

pos -= vel
seconds -= 1
display_message(pos)
print('')
print(seconds)
