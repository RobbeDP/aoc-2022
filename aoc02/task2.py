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


def get_score(opponent_move, game_result_character):
    expected_game_result = get_expected_result(game_result_character)
    move_to_play = get_move_to_play(opponent_move, expected_game_result)

    return get_game_result_score(expected_game_result) + get_move_score(move_to_play)


def get_expected_result(character):
    if character == 'X':
        return GameResult.LOSS

    if character == 'Y':
        return GameResult.DRAW

    return GameResult.WIN


def get_move_to_play(opponent_move, expected_game_result):
    if opponent_move == 'A':
        if expected_game_result == GameResult.WIN:
            return 'Y'
        if expected_game_result == GameResult.LOSS:
            return 'Z'
        return 'X'

    if opponent_move == 'B':
        if expected_game_result == GameResult.WIN:
            return 'Z'
        if expected_game_result == GameResult.LOSS:
            return 'X'
        return 'Y'

    if expected_game_result == GameResult.WIN:
        return 'X'
    if expected_game_result == GameResult.LOSS:
        return 'Y'
    return 'Z'


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
