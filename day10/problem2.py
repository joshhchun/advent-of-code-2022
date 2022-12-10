#!/usr/bin/env python3

CYCLE = 0
REG   = 1

def check_sprite():
    if (CYCLE % 40) in (REG, REG+1, REG+2):
        print('#', end='')
    else:
        print('.', end='')
    if not CYCLE % 40:
        print()

for instr in (s.strip() for s in open("input.txt").readlines()):
    y = instr.split()
    if y[0] == "addx":
        for _ in range(2):
            CYCLE += 1
            check_sprite()
        REG += int(y[1])
    else:
        CYCLE += 1
        check_sprite()

