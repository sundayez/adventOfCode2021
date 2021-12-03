def readfile(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    words = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return words


commands = list(readfile("input.txt"))

# part 1

horizontal = 0
depth = 0
for command in commands:
    [word, offset] = command.split()
    if word == "forward":
        horizontal = horizontal + int(offset)
    elif word == "down":
        depth = depth + int(offset)
    else:
        depth = depth - int(offset)

print(horizontal * depth)

# part 2

horizontal = 0
depth = 0
aim = 0
for command in commands:
    [word, offset] = command.split()
    if word == "forward":
        horizontal = horizontal + int(offset)
        depth = depth + aim * int(offset)
    elif word == "down":
        aim = aim + int(offset)
    else:
        aim = aim - int(offset)

print(horizontal * depth)
