#!/usr/bin/env python3
res = []

def main():
    instr = [x.rstrip().split(' ') for x in open("input.txt").readlines()]
    total, d = calc(instr[1:])
    print(sum(res))

def calc(instr):
    curr_dir = 0
    i = 0
    while i < len(instr):
        if instr[i][1] == "ls":
            i += 1
            while i < len(instr) and instr[i][0] != "$":
                if instr[i][0].isdigit():
                    curr_dir += int(instr[i][0])
                i += 1
            if i >= len(instr):
                if curr_dir <= 100000:
                    res.append(curr_dir)
                return (curr_dir, i)
        if instr[i][1] == "cd":
            if instr[i][2] == "..":
                if curr_dir <= 100000:
                    res.append(curr_dir)
                return (curr_dir, i)
            else:
                temp, new_i = calc(instr[i+1:])
                curr_dir += temp
                i += new_i + 1
        i += 1
    return (curr_dir, i)

if __name__ == "__main__":
    main()
