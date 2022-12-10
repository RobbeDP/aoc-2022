def main(filename):
    with open(filename) as file:
        x = 1
        cycle = 0

        for line in file:
            split_line = line.rstrip('\n').split(' ')

            cycle = do_cycles(split_line[0], x, cycle,)

            if split_line[0] == 'addx':
                x += int(split_line[1])


def do_cycles(instruction, register, current_cycle):
    cycles = {'noop': 1, 'addx': 2}

    for _ in range(cycles[instruction]):
        position = current_cycle % 40

        if position == 0:
            print()

        if position in sprite_positions(register):
            print('#', end='')
        else:
            print('.', end='')

        current_cycle += 1

    return current_cycle


def sprite_positions(middle):
    return {middle - 1, middle, middle + 1}


if __name__ == '__main__':
    main('input.txt')
