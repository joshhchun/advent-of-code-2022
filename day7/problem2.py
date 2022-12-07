#!/usr/bin/env python3
dirs = []


def main():
    instr = [x.rstrip().split(' ') for x in open("input.txt").readlines()]
    total, _ = calc(instr[1:])
    dirs.append(total)
    req_size = 30000000 - (70000000 - total)
    print(min([x for x in dirs if x >= req_size]))


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
                dirs.append(curr_dir)
                return (curr_dir, i)
        if instr[i][1] == "cd":
            if instr[i][2] == "..":
                dirs.append(curr_dir)
                return (curr_dir, i)
            else:
                temp, new_i = calc(instr[i+1:])
                curr_dir += temp
                i += new_i + 1
        i += 1
    return (curr_dir, i)


if __name__ == "__main__":
    main()
