from enum import Enum


class GameResult(Enum):
    WIN = 1
    LOSS = 2
    DRAW = 3


def main(filename):
    with open(filename) as file:
        score_sum = 0

        for line in file:
            score_sum += get_score(*line.rstrip('\n').split(' '))

        print(score_sum)


def get_score(opponent_move, your_move):
    game_result = get_game_result(opponent_move, your_move)

    return get_game_result_score(game_result) + get_move_score(your_move)


def get_game_result(opponent_move, your_move):
    if (
            opponent_move == 'A' and your_move == 'X' or
            opponent_move == 'B' and your_move == 'Y' or
            opponent_move == 'C' and your_move == 'Z'
    ):
        return GameResult.DRAW

    if (
            opponent_move == 'A' and your_move == 'Y' or
            opponent_move == 'B' and your_move == 'Z' or
            opponent_move == 'C' and your_move == 'X'
    ):
        return GameResult.WIN

    return GameResult.LOSS


def get_game_result_score(game_result):
    if game_result == GameResult.DRAW:
        return 3

    if game_result == GameResult.WIN:
        return 6

    return 0


def get_move_score(move):
    if move == 'X':
        return 1

    if move == 'Y':
        return 2

    return 3


if __name__ == '__main__':
    main('input.txt')
