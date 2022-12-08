#!/usr/bin/env python3
trees = [[int(z) for z in y.rstrip()] for y in open("input.txt").readlines()]
length = len(trees)


def scenic_score(r, c):
    score = 1
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        score *= _scenic_helper(r, c, d[0], d[1], trees[r][c])
    return score


def _scenic_helper(r, c, dy, dx, height):
    nr, nc = r + dy, c + dx
    if not 0 <= nr < length or not 0 <= nc < length:
        return 0
    elif trees[nr][nc] >= height:
        return 1
    return 1 + _scenic_helper(nr, nc, dy, dx, height)


print(max(scenic_score(r, c) for r in range(length) for c in range(length)))
