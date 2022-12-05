import re


def main(filename):
    with open(filename) as file:
        parsed_input = []
        line = file.readline().rstrip('\n')

        while not re.search(r'^ \d', line):
            crates = [line[i:i + 4] for i in range(0, len(line), 4)]
            parsed_input.append(list(map(format_crates, crates)))
            line = file.readline().rstrip('\n')

        amount = int(line[-1])
        stacks = create_stacks(parsed_input, amount)

        file.readline()

        instructions = []
        for line in file:
            matches = re.search(r'move (\d+) from (\d+) to (\d+)', line.rstrip('\n'))
            instructions.append((
                int(matches.group(1)),
                int(matches.group(2)),
                int(matches.group(3))
            ))

        perform_instructions(instructions, stacks)
        print(''.join(get_top_crates(stacks)))


def format_crates(crate):
    if crate.startswith(' '):
        return ''

    return crate.strip(' ')[1]


def create_stacks(parsed_input, amount):
    stacks = []

    for col in range(amount):
        current_stack = []
        for row in range(len(parsed_input)):
            if col < len(parsed_input[row]) and parsed_input[row][col] != '':
                current_stack.append(parsed_input[row][col])

        stacks.append(current_stack[::-1])

    return stacks


def perform_instructions(instructions, stacks):
    for instruction in instructions:
        to_move = stacks[instruction[1] - 1][len(stacks[instruction[1] - 1]) - instruction[0]:]
        stacks[instruction[2] - 1] += to_move
        stacks[instruction[1] - 1] = stacks[instruction[1] - 1][:len(stacks[instruction[1] - 1]) - instruction[0]]


def get_top_crates(stacks):
    top_crates = []

    for stack in stacks:
        top_crates.append(stack[-1])

    return top_crates


if __name__ == '__main__':
    main('test_input.txt')
