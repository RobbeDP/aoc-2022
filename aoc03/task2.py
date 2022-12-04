def main(filename):
    with open(filename) as file:
        priority_sum = 0

        current_group = []
        for line in file:
            current_group.append(line.rstrip('\n'))

            if len(current_group) == 3:
                badge_item_type = get_badge_item_type(*current_group)
                priority_sum += get_priority(badge_item_type)
                current_group = []

        print(priority_sum)


def get_badge_item_type(backpack1, backpack2, backpack3):
    intersect1 = set(backpack1).intersection(set(backpack2))
    intersect2 = intersect1.intersection(set(backpack3))

    return next(iter(intersect2))


def get_priority(character):
    ascii_value = ord(character)

    if character.islower():
        return ascii_value - 96

    return ascii_value - 38


if __name__ == '__main__':
    main('input.txt')
