import collections
import math
import re


class Monkey:
    def __init__(self, index, items, operation, test_number, true_index, false_index):
        self.index = index
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.true_index = true_index
        self.false_index = false_index


class Operation:
    def __init__(self, left, right, operation):
        self.left = left
        self.right = right
        self.operation = operation


def main(filename):
    with open(filename) as file:
        monkeys = []
        is_next = True

        while is_next:
            monkeys.append(parse_monkey(file))
            is_next = file.readline() != ''

        inspected = collections.defaultdict(int)
        lcm = math.lcm(*list(map(lambda m: m.test_number, monkeys)))

        for _ in range(10000):
            play_round(monkeys, inspected, lcm)

        sorted_counts = list(sorted(inspected.values())[::-1])
        monkey_business = sorted_counts[0] * sorted_counts[1]

        print(monkey_business)


def parse_monkey(file):
    index = re.search(r'Monkey (\d+):$', file.readline().rstrip('\n')).group(1)

    items = re.search(r'Starting items: (.*)$', file.readline().rstrip('\n')).group(1)
    items = list(map(int, items.split(', ')))

    operation = re.search(r'Operation: new = (.*)$', file.readline().rstrip('\n')).group(1)
    operation = parse_operation(operation)

    test_number = int(re.search(r'Test: divisible by (\d+)$', file.readline().rstrip('\n')).group(1))

    true_index = int(re.search(r'If true: throw to monkey (\d+)$', file.readline().rstrip('\n')).group(1))
    false_index = int(re.search(r'If false: throw to monkey (\d+)$', file.readline().rstrip('\n')).group(1))

    return Monkey(index, items, operation, test_number, true_index, false_index)


def parse_operation(operation):
    result = re.search(r'([a-z0-9]+) ([*+]) ([a-z0-9]+)', operation)

    return Operation(
        parse_operand(result.group(1)),
        parse_operand(result.group(3)),
        parse_operator(result.group(2))
    )


def parse_operand(operand):
    if operand.isnumeric():
        return int(operand)

    return operand


def parse_operator(operator):
    operator_mapping = {
        '*': lambda x, y: x * y,
        '+': lambda x, y: x + y
    }

    return operator_mapping[operator]


def play_round(monkeys, inspected, lcm):
    for index in range(len(monkeys)):
        inspected[index] += len(monkeys[index].items)
        inspect_items(index, monkeys, lcm)


def inspect_items(index, monkeys, lcm):
    current_monkey = monkeys[index]

    for item in current_monkey.items:
        worry_level = apply_operation(item, current_monkey.operation)
        worry_level %= lcm

        if worry_level % current_monkey.test_number == 0:
            index = current_monkey.true_index
        else:
            index = current_monkey.false_index

        monkeys[index].items.append(worry_level)

    current_monkey.items.clear()


def apply_operation(item, operation):
    left = item if operation.left == 'old' else operation.left
    right = item if operation.right == 'old' else operation.right

    return operation.operation(left, right)


if __name__ == '__main__':
    main('input.txt')
