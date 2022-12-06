#!/usr/bin/env python3
x = open("input.txt").read()
print([i for i in range(14, len(x)) if len(set(x[i-14:i])) == 14][0])
