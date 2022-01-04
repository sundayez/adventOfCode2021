def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


class Buffer:
    def __init__(self, fragment):
        self.fragment = fragment
        self.i = 0

    def eof(self):
        return self.i == len(self.fragment)

    def peek(self):
        c = self.fragment[self.i]
        self.i += 1
        return c

    def seek(self):
        return self.fragment[self.i]


class Operand:
    def __init__(self, number):
        self.number = number


def split_three_parts(buffer):
    c = buffer.peek()
    if c != '[':
        print("Symbol [ expected")
        return -1
    if buffer.seek() == '[':
        count = 0
        first_part = ""
        while count != 0:
            c = buffer.peek()
            first_part += c
            if c == '[':
                count += 1


def parse_buffer(buffer):
    while not buffer.eof():
        #print(buffer.peek())
        1

def part_one(lines):
    parse_buffer(Buffer(lines[0]))


def part_two(lines):
    1


def main():
    lines = read_file("input.txt")
    print(lines[0])
    part_one(lines)
    part_two(lines)


main()
