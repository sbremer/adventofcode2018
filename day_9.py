from aocd import get_data
from aocd import submit
import re

day = 9
data_raw = get_data(day=day)
m = re.match(r'(?P<n_players>.*) players; last marble is worth (?P<n_marbles>.*) points', data_raw)

n_players = int(m.group('n_players'))
n_marbles = int(m.group('n_marbles'))


def get_highscore_fast(n_players, n_marbles):
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = self
            self.next = self

        def clockwise(self):
            return self.next

        def counterclockwise(self):
            return self.prev


    marble_at = Node(0)
    players = [0] * n_players
    at_player = 0

    for marble in range(1, n_marbles + 1):
        if marble % 23 == 0:
            players[at_player] += marble

            for _ in range(7):
                marble_at = marble_at.prev

            players[at_player] += marble_at.data

            # Remove
            marble_at.next.prev = marble_at.prev
            marble_at.prev.next = marble_at.next

            marble_at = marble_at.next

        else:
            marble_at = marble_at.next

            marble_new = Node(marble)
            marble_new.next = marble_at.next
            marble_new.prev = marble_at

            marble_at.next.prev = marble_new
            marble_at.next = marble_new

            marble_at = marble_new

        at_player = (at_player + 1) % n_players


    highscore = max(players)
    return highscore


highscore = get_highscore_fast(n_players, n_marbles)
submit(highscore, level=1, day=day, year=2018)

highscore_100 = get_highscore_fast(n_players, n_marbles * 100)
submit(highscore_100, level=2, day=day, year=2018)
