#!/usr/bin/env python3

pairs = open("input.txt").readlines()
x = filter(lambda y: y[0][1] >= y[1][0], map(lambda p: sorted(p, key=lambda x: x[0]), map(lambda x: [list(map(int, x[0].split('-'))), list(map(int, x[1].split('-')))],
                                                                                          (pair.rstrip().split(',') for pair in pairs))))
