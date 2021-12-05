def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    words = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return words


def array_to_base2_number(array):
    def exp2(n):
        return 2 ** (n - 1)

    exponents = list(map(exp2, range(len(array), 0, -1)))
    return sum([x * y for x, y in zip(array, exponents)])


def count_zeros_and_ones_for_bit(binaries, bit):
    zero_count = 0
    one_count = 0
    for binary in binaries:
        if binary[bit] == '0':
            zero_count = zero_count + 1
        else:
            one_count = one_count + 1
    return [zero_count, one_count]


def count_zeros_and_ones(binaries):
    zero_count = [0] * len(binaries[0])
    one_count = [0] * len(binaries[0])
    for i in range(0, len(binaries[0])):
        [zero_count[i], one_count[i]] = count_zeros_and_ones_for_bit(binaries, i)
    return [zero_count, one_count]


def reduce_list(binaries, compare_func):
    current_bit = 0
    while len(binaries) > 1:
        [zero_count, one_count] = count_zeros_and_ones_for_bit(binaries, current_bit)
        if compare_func(zero_count, one_count):
            binaries = [binary for binary in binaries if binary[current_bit] == '0']
        else:
            binaries = [binary for binary in binaries if binary[current_bit] == '1']
        current_bit = current_bit + 1
    return array_to_base2_number([int(digit) for digit in list(binaries[0])])


def part_one(binaries):
    [zero_count, one_count] = count_zeros_and_ones(binaries)

    gamma = [0 if x > y else 1 for x, y in zip(zero_count, one_count)]
    epsilon = [0 if x < y else 1 for x, y in zip(zero_count, one_count)]
    gamma_reduced = array_to_base2_number(gamma)
    epsilon_reduced = array_to_base2_number(epsilon)
    print(gamma_reduced * epsilon_reduced)


def part_two(binaries):
    oxygen = reduce_list(binaries.copy(), lambda x, y: x > y)
    co2 = reduce_list(binaries.copy(), lambda x, y: x <= y)
    print(oxygen * co2)


def main():
    binaries = list(read_file("input.txt"))
    part_one(binaries)
    part_two(binaries)


main()
