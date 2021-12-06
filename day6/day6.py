def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def iterate_numbers(numbers):
    zeros = len([x for x in numbers if x == 0])
    numbers = [x - 1 if x > 0 else 6 for x in numbers]
    numbers = numbers + [8 for _ in range(zeros)]
    return numbers


def iterate_numbers_with_cardinality(numbers_with_cardinality):
    zeros = sum([y for x, y in numbers_with_cardinality if x == 0])
    numbers_with_cardinality = [(x - 1, y) if x > 0 else (6, y) for x, y in numbers_with_cardinality]
    numbers_with_cardinality = [(x, y) for (x, y) in
                                [(number, sum([y for x, y in numbers_with_cardinality if x == number])) for number in
                                 range(9)] if y != 0]
    if zeros != 0:
        numbers_with_cardinality.append((8, zeros))
    return numbers_with_cardinality


def part_one(numbers_with_cardinality):
    for i in range(80):
        numbers_with_cardinality = iterate_numbers_with_cardinality(numbers_with_cardinality)
    print(sum([y for (x, y) in numbers_with_cardinality]))


def part_two(numbers_with_cardinality):
    for i in range(256):
        numbers_with_cardinality = iterate_numbers_with_cardinality(numbers_with_cardinality)
    print(sum([y for (x, y) in numbers_with_cardinality]))


def main():
    lines = read_file("input.txt")
    numbers = list(map(int, lines[0].split(",")))
    numbers_with_cardinality = [(x, y) for (x, y) in
                                [(number, len([x for x in numbers if x == number])) for number in range(6)] if y != 0]
    part_one(numbers_with_cardinality)
    part_two(numbers_with_cardinality)


main()
