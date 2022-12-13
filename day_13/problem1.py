#!/usr/bin/env python3
import json
pairs = open("input.txt").read().split("\n\n")

def parse_pairs(ele1, ele2):
    if type(ele1) is int and type(ele2) is int:
        return 1 if ele1 < ele2 else (0 if ele1 == ele2 else -1)
    if type(ele1) is list and type(ele2) is list:
        for i, j in zip(ele1, ele2):
            res = parse_pairs(i, j)
            if res > 0:
                return 1
            if res < 0:
                return -1
        return 1 if len(ele1) < len(ele2) else (0 if len(ele1) == len(ele2) else -1) 
    else:
        return parse_pairs([ele1], ele2) if type(ele1) is int else parse_pairs(ele1, [ele2])


tot = 0
for i, pair in enumerate(pairs, start=1):
    ele1, ele2 = [json.loads(p) for p in pair.split("\n")]
    if parse_pairs(ele1, ele2) > 0:
        tot += i
print(tot)

