def main(filename):
    with open(filename) as file:
        pos_head = (0, 0)
        pos_tail = (0, 0)

        visited = set()
        visited.add(pos_tail)

        for line in file:
            direction, steps = line.rstrip('\n').split(' ')
            pos_head, pos_tail = move(direction, int(steps), pos_head, pos_tail, visited)

        print(len(visited))


def move(direction, steps, pos_head, pos_tail, visited):
    for _ in range(steps):
        pos_head = move_step(pos_head, direction)

        if not are_adjacent(pos_head, pos_tail):
            pos_tail = move_step_towards(pos_tail, pos_head)
            visited.add(pos_tail)

    return pos_head, pos_tail


def move_step(position, direction):
    direction_to_offset = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    dr, dc = direction_to_offset[direction]

    return position[0] + dr, position[1] + dc


def are_adjacent(pos1, pos2):
    return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1


def move_step_towards(pos_tail, pos_head):
    # Positions are in the same row
    if pos_tail[0] == pos_head[0]:
        if pos_tail[1] < pos_head[1]:
            return pos_tail[0], pos_tail[1] + 1
        else:
            return pos_tail[0], pos_tail[1] - 1

    # Positions are in the same column
    if pos_tail[1] == pos_head[1]:
        if pos_tail[0] < pos_head[0]:
            return pos_tail[0] + 1, pos_tail[1]
        else:
            return pos_tail[0] - 1, pos_tail[1]

    if pos_tail[0] < pos_head[0] and pos_tail[1] < pos_head[1]:
        return pos_tail[0] + 1, pos_tail[1] + 1
    elif pos_tail[0] < pos_head[0] and pos_tail[1] > pos_head[1]:
        return pos_tail[0] + 1, pos_tail[1] - 1
    elif pos_tail[0] > pos_head[0] and pos_tail[1] < pos_head[1]:
        return pos_tail[0] - 1, pos_tail[1] + 1
    else:
        return pos_tail[0] - 1, pos_tail[1] - 1


if __name__ == '__main__':
    main('input.txt')
