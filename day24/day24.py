def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


class InputGenerator:
    def __init__(self):
        self.digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

    def get_input(self):
        number = ''.join([str(digit) for digit in self.digits])
        for i in range(13, 0, -1):
            if self.digits[i] > 1:
                self.digits[i] -= 1
                break
            self.digits[i] = 9
        print(number)
        return number

    def has_more_inputs(self):
        return len([digit for digit in self.digits if digit != 1]) > 0


def process_input(number, instructions):
    print(number)
    return 0


def part_one(instructions):
    input_generator = InputGenerator()
    while input_generator.has_more_inputs():
        process_input(input_generator.get_input(), instructions)
    return 1


def part_two(instructions):
    return 1


def parse_input(lines):
    return [line.split(" ") for line in lines]


def main():
    lines = read_file("input.txt")
    instructions = parse_input(lines)
    part_one(instructions)
    part_two(instructions)


main()
