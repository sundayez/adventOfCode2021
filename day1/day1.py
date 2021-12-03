def readfile(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    words = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return words


numbers = list(map(int, readfile("input.txt")))

# part 1

counter = 0
for i in range(0, len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        counter = counter + 1

print(counter)

# part 2

windowedList = []
for i in range(0, len(numbers) - 2):
    windowedList.append(numbers[i] + numbers[i + 1] + numbers[i + 2])

counter = 0
for i in range(0, len(windowedList) - 1):
    if windowedList[i + 1] > windowedList[i]:
        counter = counter + 1

print(counter)
