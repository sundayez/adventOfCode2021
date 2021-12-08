def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


segments = {0: 6,  ##
            1: 2,  #
            2: 5,  ###
            3: 5,  ###
            4: 4,  #
            5: 5,  ###
            6: 6,  ##
            7: 3,  #
            8: 7,  #
            9: 6}  ##


def part_one(rules):
    count = 0
    for right_rule in [rule["right"] for rule in rules]:
        for right_digit in right_rule:
            if len(right_digit) in [segments[1], segments[4], segments[7], segments[8]]:
                count = count + 1
    print(count)


def sort(letters):
    return ''.join(sorted(letters))


def decode_wires_for_unique(left):
    association = {[sort(left_digit) for left_digit in left if len(left_digit) == 2][0]: 1,
                   [sort(left_digit) for left_digit in left if len(left_digit) == 4][0]: 4,
                   [sort(left_digit) for left_digit in left if len(left_digit) == 3][0]: 7,
                   [sort(left_digit) for left_digit in left if len(left_digit) == 7][0]: 8}

    inverse_association = {1: [sort(left_digit) for left_digit in left if len(left_digit) == 2][0],
                           4: [sort(left_digit) for left_digit in left if len(left_digit) == 4][0],
                           7: [sort(left_digit) for left_digit in left if len(left_digit) == 3][0],
                           8: [sort(left_digit) for left_digit in left if len(left_digit) == 7][0]}

    return association, inverse_association


def assign_and_remove(candidates, association, inverse_association, wire, number):
    association[wire] = number
    inverse_association[number] = wire
    candidates.remove(wire)

    return candidates, association, inverse_association


def process_with_rule(candidates, rule, inverse_association):
    return [candidate for candidate in candidates if rule(candidate, inverse_association)][0]


def decode_wires_for_length_six(left, association, inverse_association):
    digits_with_six_wires = [sort(left_digit) for left_digit in left if len(left_digit) == 6]

    six = process_with_rule(digits_with_six_wires,
                            lambda candidate, inverse_map: True if inverse_map[1][0] not in candidate or inverse_map[1][
                                1] not in candidate else False, inverse_association)

    assign_and_remove(digits_with_six_wires, association, inverse_association, six, 6)

    nine = process_with_rule(digits_with_six_wires,
                             lambda candidate, inverse_map: True if inverse_map[4][0] in candidate and inverse_map[4][
                                 1] in candidate and inverse_map[4][2] in candidate and inverse_map[4][
                                                                        3] in candidate else False,
                             inverse_association)

    assign_and_remove(digits_with_six_wires, association, inverse_association, nine, 9)
    assign_and_remove(digits_with_six_wires, association, inverse_association, digits_with_six_wires[0], 0)


def decode_wires_for_length_five(left, association, inverse_association):
    digits_with_five_wires = [sort(left_digit) for left_digit in left if len(left_digit) == 5]

    three = process_with_rule(digits_with_five_wires,
                              lambda candidate, inverse_map: True if inverse_map[1][0] in candidate and inverse_map[1][
                                  1] in candidate else False, inverse_association)

    assign_and_remove(digits_with_five_wires, association, inverse_association, three, 3)

    five = process_with_rule(digits_with_five_wires,
                             lambda candidate, inverse_map: True if candidate[0] in inverse_map[9] and candidate[1] in
                                                                    inverse_map[9] and candidate[2] in inverse_map[
                                                                        9] and candidate[3] in inverse_map[9] and
                                                                    candidate[4] in inverse_map[9] else False,
                             inverse_association)

    assign_and_remove(digits_with_five_wires, association, inverse_association, five, 5)
    assign_and_remove(digits_with_five_wires, association, inverse_association, digits_with_five_wires[0], 2)


def decode_wires(rule):
    association, inverse_association = decode_wires_for_unique(rule["left"])
    decode_wires_for_length_six(rule["left"], association, inverse_association)
    decode_wires_for_length_five(rule["left"], association, inverse_association)
    return association


def part_two(rules):
    total_sum = 0
    for rule in rules:
        association = decode_wires(rule)
        total_sum += int(''.join(map(str, [association[sort(right_code)] for right_code in rule["right"]])))

    print(total_sum)


def main():
    lines = read_file("input.txt")
    rules = [{"left": rule[0].strip().split(), "right": rule[1].strip().split()} for rule in
             [line.split("|") for line in lines]]
    part_one(rules)
    part_two(rules)


main()
