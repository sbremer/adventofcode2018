from aocd import get_data
from aocd import submit

import re

day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)
data = list(map(lambda x: int(x), data_raw.split(' ')))

sum_meta = 0


def process_node(at):
    global sum_meta

    children = data[at]
    metadata = data[at+1]

    at += 2

    for _ in range(children):
        at = process_node(at)

    for _ in range(metadata):
        meta = data[at]
        sum_meta += meta
        at += 1

    return at


at = 0
while at < len(data):
    at = process_node(at)

print(sum_meta)

submit(sum_meta, level=1, day=day, year=2018)


def process_node_2(at):
    children = data[at]
    metadata = data[at+1]

    at += 2

    value_children = []
    for _ in range(children):
        at, value = process_node_2(at)
        value_children.append(value)

    metas = []
    sum_meta = 0
    for _ in range(metadata):
        meta = data[at]
        metas.append(meta)
        sum_meta += meta
        at += 1

    if children == 0:
        value = sum_meta
    else:
        value = 0
        for meta in metas:
            if 0 < meta <= len(value_children):
                value += value_children[meta-1]

    return at, value


at = 0
while at < len(data):
    at, value = process_node_2(at)

submit(value, level=2, day=day, year=2018)
