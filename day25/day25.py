def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


class Cucumbers:
    def __init__(self, east_dictionary, south_dictionary, rows, columns):
        self.east_dictionary = east_dictionary
        self.south_dictionary = south_dictionary
        self.rows = rows
        self.columns = columns

    def __str__(self):
        return '\n'.join(
            [''.join(
                ['>' if (i, j) in self.east_dictionary else 'v' if (i, j) in self.south_dictionary else '.' for j in
                 range(self.columns)]) for i in
                range(self.rows)])

    def east_position(self, j):
        return (j + 1) % self.columns

    def south_position(self, i):
        return (i + 1) % self.rows

    def stage_east(self):
        changed = False
        new_dictionary = {}
        for east in self.east_dictionary:
            i, j = east[0], self.east_position(east[1])
            if (i, j) not in self.east_dictionary and (i, j) not in self.south_dictionary:
                changed = True
                new_dictionary[(i, j)] = ""
            else:
                new_dictionary[east] = ""
        self.east_dictionary = new_dictionary
        return changed

    def stage_south(self):
        changed = False
        new_dictionary = {}
        for south in self.south_dictionary:
            i, j = self.south_position(south[0]), south[1]
            if (i, j) not in self.east_dictionary and (i, j) not in self.south_dictionary:
                changed = True
                new_dictionary[(i, j)] = ""
            else:
                new_dictionary[south] = ""
        self.south_dictionary = new_dictionary
        return changed

    def stage(self):
        changed_east = self.stage_east()
        changed_south = self.stage_south()
        return changed_south or changed_east


def part_one(cucumbers):
    print(cucumbers)
    print("\n")
    changed = True
    i = 0
    while changed:
        changed = cucumbers.stage()
        i += 1
    print(cucumbers)
    print(i)


def part_two(cucumbers):
    return 1


def parse_input(lines):
    east_dictionary = {}
    south_dictionary = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '>':
                east_dictionary[(i, j)] = ""
            if lines[i][j] == 'v':
                south_dictionary[(i, j)] = ""
    return Cucumbers(east_dictionary, south_dictionary, len(lines), len(lines[0]))


def main():
    lines = read_file("input.txt")
    cucumbers = parse_input(lines)
    part_one(cucumbers)
    part_two(cucumbers)


main()
