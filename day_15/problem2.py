#!/usr/bin/env python3

ROW = 4000000 
x = [line.rstrip().split(" ") for line in open("input.txt").readlines()]

def parse_points(x):
    manhatten = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
    points = []
    for data in x:
        sensor = tuple(map(int, (data[2].split('=')[1][:-1], data[3].split('=')[1][:-1])))
        beacon = tuple(map(int, (data[-2].split('=')[1][:-1], data[-1].split('=')[1])))
        distance = manhatten(sensor, beacon)
        points.append((sensor, distance, beacon))
    return points

def find_line_range(sensor, beacon, distance, curr_row):
    y = abs(curr_row - sensor[1])
    if y > distance:
        return None 
    elif y == distance:
        return [sensor[0], sensor[0]]
    return [sensor[0] - (distance - y), sensor[0] + (distance - y)]

def merge_intervals(intervals):
    new_intervals = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= new_intervals[-1][1]:
            new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
        else:
            new_intervals.append(interval)
    return new_intervals

points = parse_points(x)
for i in range(ROW):
    intervals = []
    for sensor, distance, beacon in points:
        line_range = find_line_range(sensor, beacon, distance, i)
        if line_range is not None:
            intervals.append(line_range)
    intervals.sort()
    new_int = merge_intervals(intervals)
    if len(new_int) > 1:
        print((new_int[0][1] + 1) * ROW + i)
        break