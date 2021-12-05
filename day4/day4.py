# import numpy as np

def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    words = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return words


def parse_bingo(bingo_input):
    numbers_drawn = list(map(int, bingo_input[0].split(',')))
    bingo_input.remove(bingo_input[0])
    bingo_input = [list(map(int, line.split())) for line in bingo_input if line != ""]
    print(bingo_input)
    boards = []
    for i in range(0, len(bingo_input), 5):
        board = []
        for j in range(0, 5):
            board.append(bingo_input[i + j])
        boards.append(BingoBoard(board))
    return numbers_drawn, boards
    # print(boards)
    # print(boards[0])
    # print(boards[0].board[0])
    # print(boards[0].drawn)


class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.drawn = [[False for _ in range(5)] for _ in range(5)]
        self.completed = False

    def __str__(self):
        return str(self.board)

    def mark_number(self, number):
        position = [(index, row.index(number)) for index, row in enumerate(self.board) if number in row]
        if position:
            self.drawn[position[0][0]][position[0][1]] = True

    def __has_row_complete(self):
        return [True] * 5 in self.drawn

    def __has_column_complete(self):
        for j in range(len(self.drawn)):
            if [True] * 5 == [self.drawn[i][j] for i in range(len(self.drawn))]:
                return True
        return False

    def is_complete(self):
        return self.__has_row_complete() or self.__has_column_complete()

    def sum_of_unmarked(self):
        total = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if not self.drawn[i][j]:
                    total = total + self.board[i][j]
        return total


def get_winner_list(boards):
    return [board for board in boards if board.is_complete()]


def part_one():
    bingo = list(read_file("input.txt"))
    numbers_drawn, boards = parse_bingo(bingo)
    for number in numbers_drawn:
        for i in range(len(boards)):
            boards[i].mark_number(number)
        winner_list = get_winner_list(boards)
        if winner_list:
            break
    board = winner_list[0]
    print(board.sum_of_unmarked() * number)


def part_two():
    bingo = list(read_file("input.txt"))
    numbers_drawn, boards = parse_bingo(bingo)
    winners = []
    for number in numbers_drawn:
        for board in [board for board in boards if not board.completed]:
            board.mark_number(number)
            if board.is_complete():
                board.completed = True
                if len(winners) == 99:
                    print("last")
                    print(board.sum_of_unmarked() * number)
                winners.append(board)
    print(len(winners))


def main():
    part_one()
    part_two()


main()
