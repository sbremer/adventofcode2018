from aocd import get_data
from aocd import submit
from collections import defaultdict
from itertools import count
import re


day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

points = [tuple(map(lambda y:int(y), x.split(', '))) for x in data_raw.splitlines()]

margin = 5
x_min = min([x[0] for x in points]) - margin
x_max = max([x[0] for x in points]) + margin
y_min = min([x[1] for x in points]) - margin
y_max = max([x[1] for x in points]) + margin

points_active = set(points)
points_iteration = dict([(point, [point]) for point in points])
cells_size = dict([(point, 1) for point in points])
grid = defaultdict(lambda: (None, -1))

border_points = set()

growth = dict([(point, 0) for point in points])

for point in points:
    grid[point] = (point, 0)


def check_candidate(candidate):
    if candidate[0] < x_min or candidate[0] > x_max or candidate[1] < y_min or candidate[1] > y_max:
        border_points.add(point)

    elif grid[candidate][1] == -1:
        new_actives.append(candidate)
        cells_size[point] += 1
        grid[candidate] = (point, iteration)

    elif grid[candidate][1] == iteration and grid[candidate][0] != point:
        owner = grid[candidate][0]
        cells_size[owner] -= 1
        grid[candidate] = (None, -2)


for iteration in count(1):
    points_active_new = set()
    for point in points_active:
        actives = points_iteration[point]
        new_actives = []

        for active in actives:

            candidate = (active[0] + 1, active[1])
            check_candidate(candidate)

            candidate = (active[0] - 1, active[1])
            check_candidate(candidate)

            candidate = (active[0], active[1] + 1)
            check_candidate(candidate)

            candidate = (active[0], active[1] - 1)
            check_candidate(candidate)

        if len(new_actives) > 0:
            points_iteration[point] = new_actives
            points_active_new.add(point)

    points_active = points_active_new
    points_left = points_active - border_points

    if len(points_left) == 0:
        break

point_candidates = set(points) - border_points
size_candidates = [cells_size[point] for point in point_candidates]

submit(max(size_candidates), level=1, day=day, year=2018)

distance_limit = 10000

import numpy as np
man_sum = np.zeros((x_max-x_min, y_max-y_min))

points = [np.array((point[0]-x_min, point[1]-y_min)) for point in points]

for ix, iy in np.ndindex(man_sum.shape):
    at = np.array((ix, iy))
    sum = 0
    for point in points:
        sum += np.sum(np.abs(point - at))

    man_sum[ix, iy] = sum

area = np.sum(man_sum < distance_limit)

submit(area, level=2, day=day, year=2018)
