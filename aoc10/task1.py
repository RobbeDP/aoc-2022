def main(filename):
    with open(filename) as file:
        x = 1
        cycle = 0
        signal_strength = 0

        for line in file:
            split_line = line.rstrip('\n').split(' ')

            cycle, signal_strength = do_cycles(split_line[0], x, cycle, signal_strength)

            if split_line[0] == 'addx':
                x += int(split_line[1])

        print(signal_strength)


def do_cycles(instruction, register, current_cycle, signal_strength):
    checkpoints = range(20, 221, 40)
    cycles = {'noop': 1, 'addx': 2}

    for _ in range(cycles[instruction]):
        current_cycle += 1

        if current_cycle in checkpoints:
            signal_strength += current_cycle * register

    return current_cycle, signal_strength


if __name__ == '__main__':
    main('input.txt')
