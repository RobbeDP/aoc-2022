import re


def main(filename):
    with open(filename) as file:
        overlap_sum = 0

        for line in file:
            matches = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line.rstrip('\n'))
            if overlap(
                (int(matches.group(1)), int(matches.group(2))),
                (int(matches.group(3)), int(matches.group(4)))
            ):
                overlap_sum += 1

        print(overlap_sum)


def overlap(range1, range2):
    return range1[0] <= range2[0] <= range1[1] or range2[0] <= range1[0] <= range2[1]


if __name__ == '__main__':
    main('input.txt')
