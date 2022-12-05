#!/usr/bin/env python3
stacks, instr = [l.split('\n') for l in open("input.txt").read().split("\n\n")]
num_stacks = int(stacks[-1][-2])
cargo = [[] for _ in range(num_stacks)]

for stack in stacks[::-1]:
	for i, item in enumerate(stack):
		if item.isalpha():
			cargo[(i-1)//4].append(item)

for i in instr:
	num_move, from_c, to_c = [int(y) for b, y in enumerate(i.split(' ')) if b % 2]
	cargo[to_c-1].extend([cargo[from_c-1].pop() for _ in range(num_move)][::-1])

print(''.join(i.pop() for i in cargo))
