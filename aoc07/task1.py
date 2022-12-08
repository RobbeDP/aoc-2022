def main(filename):
    with open(filename) as file:
        file.readline()

        commands = []
        for line in file:
            if line.startswith('$ ls'):
                commands.append(('ls', []))
            elif line.startswith('$ cd'):
                commands.append(('cd', line[5:].rstrip()))
            else:
                commands[-1][1].append(line.rstrip('\n'))

        file_tree = parse_commands(commands)

        dir_sizes = []
        get_dirs_max_size(file_tree, dir_sizes, 100_000)

        print(sum(dir_sizes))


def parse_commands(commands):
    root = {}
    current_node = root

    for command in commands:
        if command[0] == 'ls':
            for item in command[1]:
                if item.startswith('dir'):
                    current_node[item[4:]] = {'..': current_node}
                else:
                    split_item = item.split(' ')
                    current_node[split_item[1]] = int(split_item[0])
        else:
            current_node = current_node[command[1]]

    return root


def get_dirs_max_size(current_node, dir_sizes, max_size):
    dir_sum = 0

    for name, value in current_node.items():
        if isinstance(value, int):
            dir_sum += value
        elif name != '..':
            dir_sum += get_dirs_max_size(value, dir_sizes, max_size)

    if dir_sum <= max_size:
        dir_sizes.append(dir_sum)

    return dir_sum


if __name__ == '__main__':
    main('input.txt')
