def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def parse_coordinates(lines):
    return [list(map(int, [p1.split(",")[0], p1.split(",")[1], p2.split(",")[0], p2.split(",")[1]])) for p1, p2 in
            [[a.strip(), b.strip()] for a, b in [line.split("->") for line in lines]]]


def boundaries(coordinates):
    min_x1 = min([coordinate[0] for coordinate in coordinates])
    min_y1 = min([coordinate[2] for coordinate in coordinates])
    min_x2 = min([coordinate[1] for coordinate in coordinates])
    min_y2 = min([coordinate[3] for coordinate in coordinates])
    max_x1 = max([coordinate[0] for coordinate in coordinates])
    max_y1 = max([coordinate[2] for coordinate in coordinates])
    max_x2 = max([coordinate[1] for coordinate in coordinates])
    max_y2 = max([coordinate[3] for coordinate in coordinates])
    return min(min_x1, min_x2), min(min_y1, min_y2), max(max_x1, max_x2), max(max_y1, max_y2)


class OceanMap:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        return str("\n".join(list(map(lambda line: ''.join(map(str, line)), self.board))))

    def higher_than_two(self):
        count = 0
        for row in self.board:
            for element in row:
                if element > 1:
                    count = count + 1
        return count


def part_one(coordinates):
    (xmin, ymin, xmax, ymax) = boundaries(coordinates)
    table = OceanMap([[0 for _ in range(ymax + 1)] for _ in range(xmax + 1)])
    table.board[2][3] = 1
    for (x1, y1, x2, y2) in coordinates:
        indices = []
        if x1 == x2 and y1 != y2:
            if y1 < y2:
                indices = [(x1, y) for y in range(y1, y2 + 1)]
            else:
                indices = [(x1, y) for y in range(y2, y1 + 1)]
        elif x1 != x2 and y1 == y2:
            if x1 < x2:
                indices = [(x, y1) for x in range(x1, x2 + 1)]
            else:
                indices = [(x, y1) for x in range(x2, x1 + 1)]
        for index in indices:
            table.board[index[0]][index[1]] = table.board[index[0]][index[1]] + 1
    print(table.higher_than_two())


def part_two(coordinates):
    (xmin, ymin, xmax, ymax) = boundaries(coordinates)
    table = OceanMap([[0 for _ in range(ymax + 1)] for _ in range(xmax + 1)])
    table.board[2][3] = 1
    for (x1, y1, x2, y2) in coordinates:
        indices = []
        if x1 == x2 and y1 != y2:
            if y1 < y2:
                indices = [(x1, y) for y in range(y1, y2 + 1)]
            else:
                indices = [(x1, y) for y in range(y2, y1 + 1)]
        elif x1 != x2 and y1 == y2:
            if x1 < x2:
                indices = [(x, y1) for x in range(x1, x2 + 1)]
            else:
                indices = [(x, y1) for x in range(x2, x1 + 1)]
        else:
            if x1 < x2:
                if y1 < y2:
                    indices = [(x, y) for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1))]
                else:
                    indices = [(x, y) for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1))]
            else:
                if y1 < y2:
                    indices = [(x, y) for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1))]
                else:
                    indices = [(x, y) for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 - 1, -1))]
        for index in indices:
            table.board[index[0]][index[1]] = table.board[index[0]][index[1]] + 1
    # print(table)
    print(table.higher_than_two())


def main():
    lines = read_file("input.txt")
    coordinates = parse_coordinates(lines)
    part_one(coordinates)
    part_two(coordinates)


main()
