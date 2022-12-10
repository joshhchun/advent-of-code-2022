#!/usr/bin/env python3
TIMES = (
    20, 60, 100, 140, 180, 220
)
CYCLE = 1
REG   = 1

def check_signal(curr_c):
    if curr_c in TIMES:
        signal_strengths.append(curr_c * REG)

signal_strengths = []
instrs = (s.strip().split() for s in open("input.txt").readlines())
for instr in instrs:
    check_signal(CYCLE)
    if instr[0] == "addx":
        check_signal(CYCLE + 1)
        CYCLE += 2
        REG += int(instr[1])
    else:
        CYCLE += 1

print(sum(signal_strengths))