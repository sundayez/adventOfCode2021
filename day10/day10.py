def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


symbols = {
    "p": {"opening": '(', "closing": ')', "points": 3, "points2": 1},
    "s": {"opening": '[', "closing": ']', "points": 57, "points2": 2},
    "b": {"opening": '{', "closing": '}', "points": 1197, "points2": 3},
    "a": {"opening": '<', "closing": '>', "points": 25137, "points2": 4}
}


def process_line(line):  # Returns 0 if it is complete, -1 if it is incomplete, and the value if it is incorrect
    expected_closing = []
    for element in line:
        if element == symbols["p"]["opening"]:
            expected_closing.insert(0, symbols["p"]["closing"])
        elif element == symbols["s"]["opening"]:
            expected_closing.insert(0, symbols["s"]["closing"])
        elif element == symbols["b"]["opening"]:
            expected_closing.insert(0, symbols["b"]["closing"])
        elif element == symbols["a"]["opening"]:
            expected_closing.insert(0, symbols["a"]["closing"])
        elif element == symbols["p"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["p"]["closing"]:
                return symbols["p"]["points"]
        elif element == symbols["s"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["s"]["closing"]:
                return symbols["s"]["points"]
        elif element == symbols["b"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["b"]["closing"]:
                return symbols["b"]["points"]
        elif element == symbols["a"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["a"]["closing"]:
                return symbols["a"]["points"]
    return 0 if len(expected_closing) == 0 else -1


def complete_line(line):
    expected_closing = []
    for element in line:
        if element == symbols["p"]["opening"]:
            expected_closing.insert(0, symbols["p"]["closing"])
        elif element == symbols["s"]["opening"]:
            expected_closing.insert(0, symbols["s"]["closing"])
        elif element == symbols["b"]["opening"]:
            expected_closing.insert(0, symbols["b"]["closing"])
        elif element == symbols["a"]["opening"]:
            expected_closing.insert(0, symbols["a"]["closing"])
        elif element == symbols["p"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["p"]["closing"]:
                return []
        elif element == symbols["s"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["s"]["closing"]:
                return []
        elif element == symbols["b"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["b"]["closing"]:
                return []
        elif element == symbols["a"]["closing"]:
            if len(expected_closing) == 0 or expected_closing.pop(0) != symbols["a"]["closing"]:
                return []
    return expected_closing


def part_one(lines):
    total = 0
    for line in lines:
        line_result = process_line(line)
        if line_result > 0:
            total += line_result
    print(total)


def part_two(lines):
    totals = []
    for line in lines:
        expected_closing = complete_line(line)
        total = 0
        for closing in expected_closing:
            if closing == symbols["p"]["closing"]:
                total = total * 5 + symbols["p"]["points2"]
            elif closing == symbols["s"]["closing"]:
                total = total * 5 + symbols["s"]["points2"]
            elif closing == symbols["b"]["closing"]:
                total = total * 5 + symbols["b"]["points2"]
            elif closing == symbols["a"]["closing"]:
                total = total * 5 + symbols["a"]["points2"]
        if total != 0:
            totals.append(total)
    totals.sort()
    print(totals[len(totals) // 2])


def main():
    lines = read_file("input.txt")
    part_one(lines)
    part_two(lines)


main()
