def main(filename):
    with open(filename) as file:
        priority_sum = 0

        for line in file:
            double_item = get_double_item(line.rstrip('\n'))
            priority_sum += get_priority(double_item)

        print(priority_sum)


def get_double_item(backpack):
    half = len(backpack) // 2
    compartment1 = backpack[:half]
    compartment2 = backpack[half:]

    intersect = set(compartment1).intersection(set(compartment2))

    return next(iter(intersect))


def get_priority(character):
    ascii_value = ord(character)

    if character.islower():
        return ascii_value - 96

    return ascii_value - 38


if __name__ == '__main__':
    main('input.txt')
