#!/usr/bin/env python3

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),  
    'D': (0, -1)
}

def move(pos, d):
    head, tail = pos
    # Move head
    head[0] += directions[d][0]
    head[1] += directions[d][1]

    # Move tail
    num_to_add = lambda delta: 1 if delta > 0 else -1 if delta < 0 else 0
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) > 1 or abs(dy) > 1:
        tail[0] += num_to_add(dx)
        tail[1] += num_to_add(dy)
    return tuple(tail)

pos = [[0, 0], [0, 0]]
tail_positions = set()
for line in open("input.txt").readlines():
    d, n = line.split()
    for _ in range(int(n)):
        tail_positions.add(move(pos, d))

print(len(tail_positions))
