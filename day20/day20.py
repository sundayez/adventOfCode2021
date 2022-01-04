def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


class Image:
    def __init__(self, values_dictionary, image_enhancement):
        self.values = values_dictionary
        self.enhancement = image_enhancement
        self.min_i = min([i for (i, _) in values_dictionary.keys()])
        self.max_i = max([i for (i, _) in values_dictionary.keys()])
        self.min_j = min([j for (_, j) in values_dictionary.keys()])
        self.max_j = max([j for (_, j) in values_dictionary.keys()])
        self.outer_space = '.'

    def __str__(self):
        return '\n'.join(
            [''.join(['#' if (i, j) in self.values else '.' for j in range(self.min_j, self.max_j + 1)]) for i in
             range(self.min_i, self.max_i + 1)])

    def rebind(self):
        self.min_i = min([i for (i, _) in self.values.keys()])
        self.max_i = max([i for (i, _) in self.values.keys()])
        self.min_j = min([j for (_, j) in self.values.keys()])
        self.max_j = max([j for (_, j) in self.values.keys()])

    def get_enhance_index(self, i, j):
        binary = ""
        for kk in range(i - 1, i + 2):
            for ll in range(j - 1, j + 2):
                if kk < self.min_i or ll < self.min_j or kk > self.max_i or ll > self.max_j:
                    if self.outer_space == '#':
                        binary += "1"
                    else:
                        binary += "0"
                elif (kk, ll) in self.values:
                    binary += "1"
                else:
                    binary += "0"
        return int(binary, 2)

    def enhance(self):
        new_values = {}
        for i in range(self.min_i - 1, self.max_i + 2):
            for j in range(self.min_j - 1, self.max_j + 2):
                enhance_index = self.get_enhance_index(i, j)
                if self.enhancement[enhance_index] == '#' and (i, j) not in new_values:
                    new_values[(i, j)] = ""
        self.outer_space = self.enhancement[self.get_enhance_index(-2, -2)]
        self.values = new_values
        self.rebind()


def part_one(image):
    print(image)
    print("\n")
    for i in range(2):
        image.enhance()
        print(image)
        print("\n")
    print(image)
    print(len(image.values))


def part_two(image):
    print(image)
    print("\n")
    for i in range(50):
        image.enhance()
        print(image)
        print("\n")
    print(image)
    print(len(image.values))


def parse_input(lines):
    image_enhancement = lines[0]
    values_dictionary = {}
    for i in range(2, len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                values_dictionary[(i - 2, j)] = ""
    return Image(values_dictionary, image_enhancement)


def main():
    lines = read_file("input.txt")
    image = parse_input(lines)
    part_one(image)
    image = parse_input(lines)
    part_two(image)


main()
