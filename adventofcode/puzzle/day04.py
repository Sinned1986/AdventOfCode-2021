# Day 4: Giant Squid

import numpy as np
import colorama
from functools import partial


def read_bingo_sequence(fv):
    row = fv.readline()
    string_list = row.split(',')
    int_map = map(int, string_list)
    int_list = list(int_map)
    number_sequence = int_list
    row = fv.readline()

    return number_sequence


# returns a tuple of the bingo_boards and the sequence of called numbers
def read_bingo_file():
    diagnostics = []
    with open('day/4/input.txt') as fv:

        bingo_sequence = read_bingo_sequence(fv)
        bingo_boards = []

        new_rows = []
        for row in fv:
            if len(row) == 1:
                new_board = np.stack(new_rows)
                bingo_boards.append(new_board)
                new_rows = []
            else:
                new_row = np.fromstring(row, dtype=np.int8, sep=' ')
                new_rows.append(new_row)

    return bingo_boards, bingo_sequence


# generate arrays for all bingo boards, we want to mark called numbers in those arrays
def create_bingo_history(bb):
    board_size = len(bb[0])
    bb_history = []
    for i in range(0, len(bb)):
        bb_history.append(np.zeros([board_size, board_size], dtype=bool))
    return bb_history


class EndGameException(Exception):
    def __init__(self, winner_number, game_round, used_numbers):
        self.board_index = winner_number
        self.game_round = game_round
        self.winner_numbers = used_numbers


def mark_numbers_on_board(board, numbers_to_mark):
    marked_board = np.full((len(board), len(board[0])), -1, dtype=np.int8)

    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val in numbers_to_mark:
                marked_board[y, x] = val
    return marked_board

def play_bingo(end_condition, plot_board=False):
    bbs, bs = read_bingo_file()
    bbs_h = create_bingo_history(bbs)
    bbs_done = np.zeros(len(bbs), dtype=bool)

    last_board_index = -1
    end_round = -1
    marked_numbers = []

    try:
        for game_round, called_number in enumerate(bs):
            for board_idx, board in enumerate(bbs):
                if not bbs_done[board_idx]:
                    search_result = np.where(board == called_number)
                    if len(search_result[0]) == 1:
                        bbs_h[board_idx][search_result[0], search_result[1]] = True
                        cross_h = bbs_h[board_idx][search_result[0], :]
                        cross_v = bbs_h[board_idx][:, search_result[1]]
                        if np.all(cross_h):
                            bbs_done[board_idx] = True
                            winner_numbers = np.reshape(board[search_result[0], :], -1)
                        if np.all(cross_v):
                            bbs_done[board_idx] = True
                            winner_numbers = np.reshape(board[:, search_result[1]], -1)
                        if end_condition(bbs_done):
                            raise EndGameException(board_idx, game_round, winner_numbers)
    except EndGameException as e:

        winner_board_index = e.board_index
        end_round = e.game_round
        marked_numbers = bs[:e.game_round + 1]

        if plot_board:
            print('player %2d won in round %3d with values: %r' % (e.board_index, e.game_round, e.winner_numbers))

            called_numbers_on_board = mark_numbers_on_board(bbs[e.board_index], bs[:e.game_round + 1])
            winner_numbers_on_board = mark_numbers_on_board(bbs[e.board_index], e.winner_numbers)

            color_func = partial(color_numbers, bs[:e.game_round + 1], e.winner_numbers)
            np.set_printoptions(formatter={'int': color_func}, linewidth=200)
            print('complete board:\n%r' % bbs[e.board_index])
            np.set_printoptions(formatter=None, linewidth=75)

    else:
        if plot_board:
            print('no player won')
        return -1

    unmarked_numbers = []
    for board_number in np.reshape(bbs[winner_board_index], -1):
        if board_number not in marked_numbers:
            unmarked_numbers.append(board_number)

    adventofcode_result = np.sum(unmarked_numbers) * bs[end_round]
    return adventofcode_result


def color_numbers(color1_values, color2_values, value):
    modifiers = []

    if value in color1_values:
        modifiers.append(colorama.Fore.RED)
    if value in color2_values:
        modifiers.append(colorama.Back.GREEN)

    if value in color1_values:
        modifiers.append(colorama.Fore.RESET)
    if value in color2_values:
        modifiers.append(colorama.Back.RESET)

    if len(modifiers) == 0:
        return f'{value:2}'
    if len(modifiers) == 2:
        return f'{modifiers[0]}{value:2}{modifiers[-1]}'
    if len(modifiers) == 4:
        return f'{modifiers[0]}{modifiers[1]}{value:2}{modifiers[-2]}{modifiers[-1]}'


def day04a(plot_board=False):
    return play_bingo(end_condition=np.any, plot_board=plot_board)


def day04b(plot_board=False):
    return play_bingo(end_condition=np.all, plot_board=plot_board)


if __name__ == '__main__':
    print(day04a(plot_board=True))
    print(day04b(plot_board=True))
