def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def build_polymer_dict(polymer):
    polymer_dict = {}
    for i in range(len(polymer) - 1):
        sub = ''.join([polymer[i], polymer[i + 1]])
        if sub in polymer_dict:
            polymer_dict[sub] += 1
        else:
            polymer_dict[sub] = 1
    return polymer_dict


def calculate_frequencies(polymer_dict, rules, iterations):
    for i in range(iterations):
        new_dict = {}
        for key in polymer_dict.keys():
            sub1 = key[0] + rules[key]
            sub2 = rules[key] + key[1]
            if sub1 in new_dict:
                new_dict[sub1] += polymer_dict[key]
            else:
                new_dict[sub1] = polymer_dict[key]
            if sub2 in new_dict:
                new_dict[sub2] += polymer_dict[key]
            else:
                new_dict[sub2] = polymer_dict[key]
        polymer_dict = new_dict
    frequencies = {}
    for polymer in polymer_dict:
        if polymer[1] in frequencies:
            frequencies[polymer[1]] += polymer_dict[polymer]
        else:
            frequencies[polymer[1]] = polymer_dict[polymer]
    frequencies[polymer[0]] += 1
    return frequencies


def calculate_problem(polymer, rules, iterations):
    polymer_dict = build_polymer_dict(polymer)
    frequencies = calculate_frequencies(polymer_dict, rules, iterations)
    print(max(frequencies.values()) - min(frequencies.values()))


def part_one(polymer, rules):
    calculate_problem(polymer, rules, 10)


def part_two(polymer, rules):
    calculate_problem(polymer, rules, 40)


def parse_lines(lines):
    polymer = lines[0]
    rules = {rule[0].strip(): rule[1].strip() for rule in [line.split('->') for line in lines[2:]]}
    return polymer, rules


def main():
    lines = read_file("input.txt")
    polymer, rules = parse_lines(lines)
    part_one(polymer, rules)
    part_two(polymer, rules)


main()
