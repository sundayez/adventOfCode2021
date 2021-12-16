def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def matrix_to_string(matrix):
    return '\n'.join([''.join(map(str, row)) for row in matrix])


def increase_row(row, d):
    return [number + d if number + d <= 9 else number + d - 9 for number in row]


class Numbers:
    def __init__(self, values):
        self.values = values
        self.distances = [[10000000000000 for _ in range(len(self.values[0]))] for _ in range(len(self.values))]
        self.parent = {}
        self.visited = [[False for _ in range(len(self.values[0]))] for _ in range(len(self.values))]

    def __str__(self):
        return matrix_to_string(self.values)

    def grow(self):
        for i in range(len(self.values)):
            self.values[i] += increase_row(self.values[i], 1) + increase_row(self.values[i], 2) + increase_row(
                self.values[i], 3) + increase_row(self.values[i], 4)
        original_size = len(self.values)
        for i in range(4):
            for j in range(original_size):
                self.values.append(increase_row(self.values[original_size * i + j], 1))
        self.distances = [[10000000000000 for _ in range(len(self.values[0]))] for _ in range(len(self.values))]
        self.parent = {}
        self.visited = [[False for _ in range(len(self.values[0]))] for _ in range(len(self.values))]

    def dijkstra(self, source):
        self.distances[source[0]][source[1]] = 0
        queue = {(source[0], source[1]): self.distances[source[0]][source[1]]}
        while len(queue) != 0:
            u = min(queue, key=queue.get)
            queue.pop(u)
            print("remaining {}".format(len(queue)))
            self.visited[u[0]][u[1]] = True
            if u[0] > 0 and not self.visited[u[0] - 1][u[1]]:
                if self.distances[u[0] - 1][u[1]] > self.distances[u[0]][u[1]] + self.values[u[0] - 1][u[1]]:
                    self.distances[u[0] - 1][u[1]] = self.distances[u[0]][u[1]] + self.values[u[0] - 1][u[1]]
                    self.parent[(u[0] - 1, u[1])] = (u[0], u[1])
                    queue[(u[0] - 1, u[1])] = self.distances[u[0] - 1][u[1]]
            if u[0] < len(self.values) - 1 and not self.visited[u[0] + 1][u[1]]:
                if self.distances[u[0] + 1][u[1]] > self.distances[u[0]][u[1]] + self.values[u[0] + 1][u[1]]:
                    self.distances[u[0] + 1][u[1]] = self.distances[u[0]][u[1]] + self.values[u[0] + 1][u[1]]
                    self.parent[(u[0] + 1, u[1])] = (u[0], u[1])
                    queue[(u[0] + 1, u[1])] = self.distances[u[0] + 1][u[1]]
            if u[1] > 0 and not self.visited[u[0]][u[1] - 1]:
                if self.distances[u[0]][u[1] - 1] > self.distances[u[0]][u[1]] + self.values[u[0]][u[1] - 1]:
                    self.distances[u[0]][u[1] - 1] = self.distances[u[0]][u[1]] + self.values[u[0]][u[1] - 1]
                    self.parent[(u[0], u[1] - 1)] = (u[0], u[1])
                    queue[(u[0], u[1] - 1)] = self.distances[u[0]][u[1] - 1]
            if u[1] < len(self.values) - 1 and not self.visited[u[0]][u[1] + 1]:
                if self.distances[u[0]][u[1] + 1] > self.distances[u[0]][u[1]] + self.values[u[0]][u[1] + 1]:
                    self.distances[u[0]][u[1] + 1] = self.distances[u[0]][u[1]] + self.values[u[0]][u[1] + 1]
                    self.parent[(u[0], u[1] + 1)] = (u[0], u[1])
                    queue[(u[0], u[1] + 1)] = self.distances[u[0]][u[1] + 1]


def part_one(numbers):
    print(numbers)
    numbers.dijkstra((0, 0))
    print(numbers.distances[len(numbers.distances) - 1][len(numbers.distances[0]) - 1])


def part_two(numbers):
    numbers.grow()
    print(numbers)
    numbers.dijkstra((0, 0))
    print(numbers.distances[len(numbers.distances) - 1][len(numbers.distances[0]) - 1])


def main():
    lines = read_file("input.txt")
    numbers = Numbers([list(map(int, str(line))) for line in lines])
    part_one(numbers)
    part_two(numbers)


main()
