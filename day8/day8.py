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


def part_two(rules):
    total_sum = 0
    for rule in rules:
        association = {[sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 2][0]: 1,
                       [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 4][0]: 4,
                       [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 3][0]: 7,
                       [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 7][0]: 8}

        inverse_association = {1: [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 2][0],
                               4: [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 4][0],
                               7: [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 3][0],
                               8: [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 7][0]}

        digits_with_six_wires = [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 6]

        six = [candidate for candidate in digits_with_six_wires if
               inverse_association[1][0] not in candidate or inverse_association[1][1] not in candidate][0]

        association[six] = 6
        inverse_association[6] = six
        digits_with_six_wires.remove(six)

        nine = [candidate for candidate in digits_with_six_wires if
                inverse_association[4][0] in candidate and inverse_association[4][1] in candidate and
                inverse_association[4][2] in candidate and inverse_association[4][3] in candidate][0]

        association[nine] = 9
        inverse_association[9] = nine
        digits_with_six_wires.remove(nine)

        association[digits_with_six_wires[0]] = 0
        inverse_association[0] = digits_with_six_wires[0]

        digits_with_five_wires = [sort(left_digit) for left_digit in rule["left"] if len(left_digit) == 5]
        three = [candidate for candidate in digits_with_five_wires if
                 inverse_association[1][0] in candidate and inverse_association[1][1] in candidate][0]

        association[three] = 3
        inverse_association[3] = three

        digits_with_five_wires.remove(three)

        five = [candidate for candidate in digits_with_five_wires if
                candidate[0] in inverse_association[9] and candidate[1] in inverse_association[9] and candidate[2] in
                inverse_association[9] and candidate[3] in inverse_association[9] and candidate[4] in
                inverse_association[9]][0]

        association[five] = 5
        inverse_association[5] = five

        digits_with_five_wires.remove(five)

        association[digits_with_five_wires[0]] = 2
        inverse_association[2] = digits_with_five_wires[0]

        total_sum += int(''.join(map(str, [association[sort(right_code)] for right_code in rule["right"]])))

    print(total_sum)


def main():
    lines = read_file("input.txt")
    rules = [{"left": rule[0].strip().split(), "right": rule[1].strip().split()} for rule in
             [line.split("|") for line in lines]]
    part_one(rules)
    part_two(rules)


main()
