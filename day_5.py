from aocd import get_data
from aocd import submit
import re


def get_poly_length(sequence):
    changed = True
    while changed:
        at = 0
        changed = False
        while at + 1 < len(sequence):
            if abs(ord(sequence[at]) - ord(sequence[at + 1])) == 32:
                changed = True
                sequence.pop(at)
                sequence.pop(at)
            else:
                at += 1
    return len(sequence)


day = re.findall("day_(.*?).py", __file__)[0]
data_raw = get_data(day=day)

sequence = list(data_raw)

poly_len = get_poly_length(sequence)

submit(poly_len, level=1, day=day, year=2018)

letters = set(data_raw.lower())
poly_len_min = len(data_raw)

for letter in letters:
    sequence = list(data_raw.replace(letter, '').replace(letter.upper(), ''))

    poly_len = get_poly_length(sequence)
    if poly_len < poly_len_min:
        poly_len_min = poly_len

submit(poly_len_min, level=2, day=day, year=2018)
