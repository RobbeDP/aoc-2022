def main(filename):
    with open(filename) as file:
        grid = []

        for line in file:
            grid.append([int(char) for char in line.rstrip('\n')])

        print(get_scenic_score_sum(grid))


def get_scenic_score_sum(grid):
    max_scenic_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            scenic_score = calculate_scenic_score(grid, row, col)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def tree_on_edge(grid, row, col):
    return row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1


def outside_grid(grid, row, col):
    return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])


def calculate_scenic_score(grid, row, col):
    if tree_on_edge(grid, row, col):
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    scenic_score = 1

    for direction in directions:
        view_distance = 0
        curr_row, curr_col = row + direction[0], col + direction[1]

        while not outside_grid(grid, curr_row, curr_col):
            view_distance += 1

            if grid[row][col] <= grid[curr_row][curr_col]:
                break

            curr_row, curr_col = curr_row + direction[0], curr_col + direction[1]

        scenic_score *= view_distance

    return scenic_score


if __name__ == '__main__':
    main('input.txt')
