#!/usr/bin/env python3
import json
from functools import cmp_to_key

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

packets = [json.loads(p) for pair in pairs for p in pair.split("\n")] + [[[2]], [[6]]]
sorted_packets = sorted(packets, key=cmp_to_key(parse_pairs), reverse=True)

res = 1
for i, packet in enumerate(sorted_packets, start=1):
    if packet == [[2]] or packet == [[6]]:
        res *= i
print(res)