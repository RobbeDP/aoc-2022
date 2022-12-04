import re


def main(filename):
    with open(filename) as file:
        overlap_sum = 0

        for line in file:
            matches = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line.rstrip('\n'))
            if fully_overlap(
                (int(matches.group(1)), int(matches.group(2))),
                (int(matches.group(3)), int(matches.group(4)))
            ):
                overlap_sum += 1

        print(overlap_sum)


def fully_overlap(range1, range2):
    range1 = range(range1[0], range1[1] + 1)
    range2 = range(range2[0], range2[1] + 1)

    return fully_overlap_one_way(range1, range2) or fully_overlap_one_way(range2, range1)


def fully_overlap_one_way(range1, range2):
    return range1.start in range2 and range1[-1] in range2


if __name__ == '__main__':
    main('input.txt')
