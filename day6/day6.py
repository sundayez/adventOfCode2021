def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def iterate_numbers(numbers):
    zeros = sum([y for x, y in numbers if x == 0])
    numbers = [(x - 1, y) if x > 0 else (6, y) for x, y in numbers]
    numbers = [(x, y) for (x, y) in
               [(number, sum([y for x, y in numbers if x == number])) for number in
                range(9)] if y != 0]
    if zeros != 0:
        numbers.append((8, zeros))
    return numbers


def process(numbers, iterations):
    for i in range(iterations):
        numbers = iterate_numbers(numbers)
    return sum([y for (x, y) in numbers])


def part_one(numbers):
    print(process(numbers, 80))


def part_two(numbers):
    print(process(numbers, 256))


def main():
    lines = read_file("input.txt")
    numbers = [(x, y) for (x, y) in
               [(number, len([x for x in list(map(int, lines[0].split(","))) if x == number])) for number in range(6)]
               if y != 0]
    part_one(numbers)
    part_two(numbers)


main()
