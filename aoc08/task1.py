def main(filename):
    with open(filename) as file:
        grid = []

        for line in file:
            grid.append([int(char) for char in line.rstrip('\n')])

        print(get_visible_tree_amount(grid))


def get_visible_tree_amount(grid):
    tree_amount = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if tree_on_edge(grid, row, col) or tree_visible(grid, row, col):
                tree_amount += 1

    return tree_amount


def tree_on_edge(grid, row, col):
    return row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1


def outside_grid(grid, row, col):
    return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])


def tree_visible(grid, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        curr_row, curr_col = row + direction[0], col + direction[1]

        found = True
        while not outside_grid(grid, curr_row, curr_col):
            if grid[curr_row][curr_col] >= grid[row][col]:
                found = False
                break

            curr_row, curr_col = curr_row + direction[0], curr_col + direction[1]

        if found:
            return True


if __name__ == '__main__':
    main('input.txt')
