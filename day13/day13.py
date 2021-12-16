def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def part_one(paper, folds):
    #print(paper)
    print(folds)
    for fold in folds:
        if fold[0] == 'x':
            paper.fold_x()
        else:
            paper.fold_y()
        print(paper.count_points())
        print("\n")
    print(paper)
    print(paper.count_points())


def part_two(paper, folds):
    1


def get_boundaries(coordinate_lines):
    x_coordinates = [p[0] for p in coordinate_lines]
    y_coordinates = [p[1] for p in coordinate_lines]
    return max(x_coordinates) + 1, max(y_coordinates) + 1


class Paper:
    def __init__(self, coordinate_lines):
        boundaries = get_boundaries(coordinate_lines)
        self.values = [['.' for _ in range(boundaries[0])] for _ in range(boundaries[1])]
        for line in coordinate_lines:
            self.values[line[1]][line[0]] = '#'

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.values])

    def fold_x(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[i]) // 2):
                self.values[i][j] = self.__carbon_paper(i, j, i, len(self.values[i]) - j - 1)
        for row in self.values:
            del row[-len(row) // 2:]

    def fold_y(self):
        for i in range(len(self.values) // 2):
            for j in range(len(self.values[i])):
                self.values[i][j] = self.__carbon_paper(i, j, len(self.values) - i - 1, j)
        del self.values[-len(self.values) // 2:]

    def __carbon_paper(self, i1, j1, i2, j2):
        if self.values[i1][j1] == '#' or self.values[i2][j2] == '#':
            return '#'
        return '.'

    def count_points(self):
        count = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if self.values[i][j] == '#':
                    count += 1
        return count


def parse_lines(lines):
    coordinate_lines = [list(map(int, coordinate.split(','))) for coordinate in
                        [line for line in lines if len(line) != 0 and line[0] != 'f']]
    folds = [[fold_line[0][-1:], int(fold_line[1])] for fold_line in
             [fold.split('=') for fold in [line for line in lines if len(line) != 0 and line[0] == 'f']]]
    return Paper(coordinate_lines), folds


def main():
    lines = read_file("input.txt")
    paper, folds = parse_lines(lines)
    part_one(paper, folds)
    part_two(paper, folds)


main()
