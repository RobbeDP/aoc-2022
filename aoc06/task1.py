def main(filename):
    with open(filename) as file:
        data = file.readline()
        print(get_marker_position(data, 4))


def get_marker_position(data, length):
    for i in range(len(data) - length + 1):
        if len(set(data[i:i+length])) == length:
            return i + length


if __name__ == '__main__':
    main('input.txt')
