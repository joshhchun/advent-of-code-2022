#!/usr/bin/env python3

ROW = 2000000
x = [line.rstrip().split(" ") for line in open("input.txt").readlines()]

def parse_points(x):
    manhatten = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
    points = []
    for data in x:
        sensor = tuple(map(int, (data[2].split('=')[1][:-1], data[3].split('=')[1][:-1])))
        beacon = tuple(map(int, (data[-2].split('=')[1][:-1], data[-1].split('=')[1])))
        distance = manhatten(sensor, beacon)
        yield (sensor, distance, beacon)


def fill_row(sensor, grid, distance, beacon):
    curr_dist = abs(sensor[1] - ROW)
    if curr_dist <= distance:
        start_x = sensor[0] - (distance - curr_dist)
        end_x = sensor[0] + (distance - curr_dist)
        for x in range(start_x, end_x + 1):
            if (x, ROW) != beacon:
                grid.add((x, ROW))
    
lines = parse_points(x)
grid = set()
for data in lines:
    sensor, distance, beacon = data
    fill_row(sensor, grid, distance, beacon)

print(len(grid))