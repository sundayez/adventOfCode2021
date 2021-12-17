def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def part_one(polymer, rules):
    for i in range(10):
        print(i)
        new_polymer = polymer[0]
        for j in range(len(polymer) - 1):
            sub = ''.join([polymer[j], polymer[j + 1]])
            if rules[sub]:
                new_polymer += rules[sub]
                new_polymer += sub[1]
            else:
                new_polymer += sub[1]
        polymer = new_polymer
    print(len(polymer))
    freqs = {}
    for c in polymer:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    print(max(freqs.values()) - min(freqs.values()))


def part_two(polymer, rules):
    for i in range(40):
        print(i)
        new_polymer = polymer[0]
        for j in range(len(polymer) - 1):
            sub = ''.join([polymer[j], polymer[j + 1]])
            if rules[sub]:
                new_polymer += rules[sub]
                new_polymer += sub[1]
            else:
                new_polymer += sub[1]
        polymer = new_polymer
    print(len(polymer))
    freqs = {}
    for c in polymer:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    print(max(freqs.values()) - min(freqs.values()))


def parse_lines(lines):
    polymer = lines[0]
    rules = {rule[0].strip(): rule[1].strip() for rule in [line.split('->') for line in lines[2:]]}
    return polymer, rules


def main():
    lines = read_file("input.txt")
    polymer, rules = parse_lines(lines)
    part_one(polymer, rules)
    # part_two(polymer, rules)


main()
