#!/usr/bin/env python3
from collections import deque


def handle_op(num1: int, num2: int, op: str) -> int:
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
            if monkey == "humn":
                continue
            monkeys[monkey] = int(line[1])
    return monkeys, stack

# Maybe clean up, find someway to utilize `handle_op` function


def find_missing(monk, stack, monkeys):
    from_monk, monk1, op, monk2 = monk
    target = monkeys[from_monk]
    if monk1 not in monkeys and monk2 in monkeys:
        if op == '/':
            target = target * monkeys[monk2]
        elif op == "*":
            target = target // monkeys[monk2]
        elif op == "+":
            target = target - monkeys[monk2]
        else:
            target = target + monkeys[monk2]
        monkeys[monk1] = target
        if monk1 == "humn":
            return
        find_missing(stack.pop(), stack, monkeys)
    elif monk2 not in monkeys and monk1 in monkeys:
        if op == '/':
            target = monkeys[monk1] // target
        elif op == "*":
            target = target // monkeys[monk1]
        elif op == "+":
            target = target - monkeys[monk1]
        else:
            target = monkeys[monk1] - target
        monkeys[monk2] = target
        if monk2 == "humn":
            return
        find_missing(stack.pop(), stack, monkeys)


def main():
    monkeys, stack = parse_monkeys()
    humn_stack = deque()
    target_monk = "humn"
    while stack:
        from_monk, monk1, op, monk2 = stack.popleft()
        if from_monk == "root":
            root_monk = (monk1, monk2)
            continue
        if monk1 == target_monk or monk2 == target_monk:
            humn_stack.append((from_monk, monk1, op, monk2))
            target_monk = from_monk
            continue
        if monk1 not in monkeys or monk2 not in monkeys:
            stack.append((from_monk, monk1, op, monk2))
            continue
        else:
            monkeys[from_monk] = handle_op(monkeys[monk1], monkeys[monk2], op)

    if root_monk[0] in monkeys:
        monkeys[root_monk[1]] = monkeys[root_monk[0]]
    else:
        monkeys[root_monk[0]] = monkeys[root_monk[1]]

    find_missing(humn_stack.pop(), humn_stack,
                 monkeys)

    print(monkeys['humn'])


if __name__ == "__main__":
    main()
