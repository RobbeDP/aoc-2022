def main(filename):
    with open(filename) as file:
        sums = []
        current_sum = 0

        for line in file:
            line = line.rstrip('\n')

            if line == '':
                sums.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line)

    sums.append(current_sum)
    sums = sorted(sums)[::-1]
    print(sum(sums[:3]))


if __name__ == '__main__':
    main('input.txt')
