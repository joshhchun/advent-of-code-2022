#!/usr/bin/env python3
from collections import deque
lines = [list(l.rstrip()) for l in open("input.txt").readlines()]

def set_points(lines):
    start_points = []
    end_point = None
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == 'S':
                lines[row][col] = 'a'
                start_points.append((row, col))
            if lines[row][col] == 'a':
                start_points.append((row, col))
            elif lines[row][col] == 'E':
                lines[row][col] = 'z'
                end_point = (row, col)
    return (start_points, end_point)
    
def find_shortest_path(start_points, end_point, lines):
    positions = deque([(point, 0) for point in start_points])
    visited = set()

    while positions:
        curr_pos, steps = positions.popleft()
        row, col = curr_pos
        if curr_pos == end_point:
            return steps
        if curr_pos in visited:
            continue
        visited.add(curr_pos) 
        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row, new_col = row + direction[0], col + direction[1]
            if new_row < 0 or new_col < 0 or new_row >= len(lines) or new_col >= len(lines[0]):
                continue
            if ord(lines[new_row][new_col]) <= ord(lines[row][col]) + 1:
                positions.append(((new_row, new_col), steps + 1))
    return None 

start_points, end_point = set_points(lines)
print(find_shortest_path(start_points, end_point, lines))