#!/usr/bin/env python3
x = open("input.txt").read()
print([i for i in range(4, len(x)) if len(set(x[i-4:i])) == 4][0])
