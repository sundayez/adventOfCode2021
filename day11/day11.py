def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def print_numbers_pretty(numbers):
    for row in numbers:
        print(str(row))
    print("\n")


def propagate(numbers, i, j):
    for kk in range(max(0, i - 1), min(i + 2, len(numbers))):
        for ll in range(max(0, j - 1), min(j + 2, len(numbers[i]))):
            if kk != i or ll != j:
                if numbers[kk][ll] != 0:
                    numbers[kk][ll] += 1
                    if numbers[kk][ll] > 9:
                        numbers[kk][ll] = 0
                        propagate(numbers, kk, ll)


def flashes_by_step(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            numbers[i][j] += 1

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] > 9:
                numbers[i][j] = 0
                propagate(numbers, i, j)
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] == 0:
                total += 1
    return total


def part_one(numbers):
    print_numbers_pretty(numbers)
    total = 0
    for i in range(100):
        total += flashes_by_step(numbers)
    print_numbers_pretty(numbers)
    print(total)


def part_two(numbers):
    print_numbers_pretty(numbers)
    i = 1
    while flashes_by_step(numbers) != 100:
        i += 1
    print(i)


def main():
    lines = read_file("input.txt")
    numbers = [list(map(int, str(line))) for line in lines]
    part_one(numbers)
    numbers = [list(map(int, str(line))) for line in lines]
    part_two(numbers)


main()
