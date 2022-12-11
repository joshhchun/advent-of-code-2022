#!/usr/bin/env python3
import collections
from functools import reduce

class Monkey:
    def __init__(self, id, items, op, test):
        self.inspections = 0
        self.items = collections.deque(items)
        self.op = self.find_op(op)
        self.test = self.find_test(test)

    def find_test(self, test):
        lines = [x.lstrip() for x in test]
        divisor = int(lines[0].split(" ")[3])
        true_case = int(lines[1].split(" ")[5])
        false_case = int(lines[2].split(" ")[5])
        return lambda x: true_case if not x % divisor else false_case

    def find_op(self, op):
        old_num, new_op, new_num = op
        new_num = int(new_num) if new_num.isdigit() else 0 
        if new_op == '+':
            return (lambda x: x + new_num) if new_num else lambda x: x + x
        elif new_op == '-':
            return (lambda x: x - new_num) if new_num else lambda x: x - x
        elif new_op == '*':
            return (lambda x: x * new_num) if new_num else lambda x: x * x
        elif new_op == '/':
            return (lambda x: x // new_num) if new_num else lambda x: x // x

def parse_monkeys(monkeys):
    for line in open("input.txt").read().split("\n\n"):
        info = [l.lstrip() for l in line.split("\n")]
        items = [int(x) for x in info[1].split(' ', 2)[2].split(',')]
        op = info[2].split(' ')[3:]
        monkeys.append(Monkey(id, items, op, info[3:]))

def inspect(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspections += 1
                item = monkey.items.popleft()
                worry_level = monkey.op(item) // 3
                monkeys[monkey.test(worry_level)].items.append(worry_level)

def main():
    monkeys = []
    parse_monkeys(monkeys)
    inspect(monkeys)
    print(reduce(lambda x, y: x * y, sorted([x.inspections for x in monkeys])[-2:]))


if __name__ == "__main__":
    main()

    