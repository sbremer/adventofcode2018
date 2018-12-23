from aocd import get_data
from aocd import submit
import re
import sys
import numpy as np


def parse_line(line):
    m = re.match(r'#(?P<id>.*) @ (?P<x>.*),(?P<y>.*): (?P<width>.*)x(?P<height>.*)', line)
    id = int(m.group('id'))
    x = int(m.group('x'))
    y = int(m.group('y'))
    width = int(m.group('width'))
    height = int(m.group('height'))

    return id, (x, y), (width, height)


day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

lines = data_raw.splitlines()

x_min = sys.maxsize
y_min = sys.maxsize
x_max = -sys.maxsize - 1
y_max = -sys.maxsize - 1

claims = []

for line in lines:
    id, pos, size = parse_line(line)

    x_min = min(pos[0], x_min)
    y_min = min(pos[1], y_min)

    x_max = max(pos[0] + size[0], x_max)
    y_max = max(pos[1] + size[1], y_max)

    claims.append((id, pos, size))

size = (x_max - y_min, y_max - y_min)
sheet = np.zeros(size)

for id, pos, size in claims:
    x = pos[0] - x_min
    x_ = x + size[0]
    y = pos[1] - y_min
    y_ = y + size[1]
    sheet[x:x_, y:y_] += 1

overlapping = np.count_nonzero(sheet > 1)

submit(overlapping, level=1, day=day, year=2018)

id_no_overlap = -1

for id, pos, size in claims:
    x = pos[0] - x_min
    x_ = x + size[0]
    y = pos[1] - y_min
    y_ = y + size[1]
    if np.all(sheet[x:x_, y:y_] == 1):
        id_no_overlap = id
        break

if id_no_overlap != -1:
    submit(id_no_overlap, level=2, day=day, year=2018)
