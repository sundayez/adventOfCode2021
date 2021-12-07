def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def align_cost(numbers, goal):
    return sum([abs(x - goal) for x in numbers])


def align_cost_2(numbers, goal):
    return sum([(1 + abs(x - goal)) * abs(x - goal) // 2 for x in numbers])


def find_min(numbers, func):
    min_value = min(numbers)
    max_value = max(numbers)
    min_align = func(numbers, min_value)
    for number in range(min_value + 1, max_value + 1):
        current_align = func(numbers, number)
        min_align = current_align if current_align < min_align else min_align
    return min_align


def part_one(numbers):
    min_align = find_min(numbers, align_cost)
    print("min align: {}".format(min_align))


def part_two(numbers):
    min_align = find_min(numbers, align_cost_2)
    print("min align: {}".format(min_align))


def main():
    lines = read_file("input.txt")
    numbers = list(map(int, lines[0].split(",")))
    part_one(numbers)
    part_two(numbers)


main()
