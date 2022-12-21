#!/usr/bin/env python3
from collections import deque


def handle_op(monk1: str, monk2: str, op: str, monkeys: dict[str, int]) -> int:
    num1 = monkeys[monk1]
    num2 = monkeys[monk2]
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 // num2
    return num1 * num2


def parse_monkeys() -> tuple[dict[str, int], deque[tuple[str, str, str, str]]]:
    stack = deque()
    monkeys = {}
    for x in open("input.txt").readlines():
        line = x.rstrip().split(" ")
        monkey = line[0][:4]
        if len(line) > 2:
            item = tuple([monkey, line[1], line[2], line[3]])
            stack.append(item)
        else:
            monkeys[monkey] = int(line[1])
    return monkeys, stack


def main():
    monkeys, stack = parse_monkeys()

    while stack:
        from_monk, monk1, op, monk2 = stack.popleft()
        if monk1 not in monkeys or monk2 not in monkeys:
            stack.append((from_monk, monk1, op, monk2))
            continue
        else:
            monkeys[from_monk] = handle_op(monk1, monk2, op, monkeys)
        if from_monk == "root":
            print(monkeys[from_monk])


if __name__ == "__main__":
    main()
