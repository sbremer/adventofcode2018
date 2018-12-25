from aocd import get_data
import numpy as np

day = 11
data_raw = get_data(day=day)

grid_sn = int(data_raw)

N = 300
level = np.zeros((N, N)).astype(int)

for x, y in np.ndindex(level.shape):
    pl = ((x + 11) * (y + 1) + grid_sn) * (x + 11)
    pl = int('{:03d}'.format(pl)[-3]) - 5
    level[x, y] = pl


def max_square(n):
    sum_max = 0
    pos = ''
    for x, y in np.ndindex((N-n+1, N-n+1)):
        sum = np.sum(level[x:x+n, y:y+n])
        if sum > sum_max:
            sum_max = sum
            pos = '{},{}'.format(x+1, y+1)
    return pos, sum_max


pos_max, sum_max = max_square(3)

print(pos_max, sum_max)

pos_max = ''
sum_max = 0
for n in range(1, 300):
    print('At: ', n)
    pos, sum = max_square(n)
    if sum > sum_max:
        sum_max = sum
        pos_max = pos + ',' + str(n)

print(pos_max, sum_max)
