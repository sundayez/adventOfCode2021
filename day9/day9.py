def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


def is_min(depth_matrix, i, j):
    if i > 0 and depth_matrix[i][j] >= depth_matrix[i - 1][j]:
        return False
    if i < len(depth_matrix) - 1 and depth_matrix[i][j] >= depth_matrix[i + 1][j]:
        return False
    if j > 0 and depth_matrix[i][j] >= depth_matrix[i][j - 1]:
        return False
    if j < len(depth_matrix[i]) - 1 and depth_matrix[i][j] >= depth_matrix[i][j + 1]:
        return False
    return True


def part_one(depth_matrix):
    count = 0
    positions = []
    for i in range(len(depth_matrix)):
        for j in range(len(depth_matrix[i])):
            if is_min(depth_matrix, i, j):
                count += 1 + depth_matrix[i][j]
                positions.append((i, j))
    print(count)
    print(positions)
    return positions


def flood(position, depth_matrix, counted):
    result = 1  # current position
    counted.append(position)
    if position[0] > 0 and depth_matrix[position[0]][position[1]] < depth_matrix[position[0] - 1][position[1]] and depth_matrix[position[0] - 1][position[1]] != 9 and (position[0] - 1, position[1]) not in counted:
        result += flood((position[0] - 1, position[1]), depth_matrix, counted)
    if position[0] < len(depth_matrix) - 1 and depth_matrix[position[0]][position[1]] < depth_matrix[position[0] + 1][position[1]] and depth_matrix[position[0] + 1][position[1]] != 9  and (position[0] + 1, position[1]) not in counted:
        result += flood((position[0] + 1, position[1]), depth_matrix, counted)
    if position[1] > 0 and depth_matrix[position[0]][position[1]] < depth_matrix[position[0]][position[1] - 1] and depth_matrix[position[0]][position[1] - 1] != 9  and (position[0], position[1]-1) not in counted:
        result += flood((position[0], position[1] - 1), depth_matrix, counted)
    if position[1] < len(depth_matrix[position[0]]) - 1 and depth_matrix[position[0]][position[1]] < depth_matrix[position[0]][position[1] + 1] and depth_matrix[position[0]][position[1] + 1] != 9  and (position[0], position[1]+1) not in counted:
        result += flood((position[0], position[1] + 1), depth_matrix, counted)
    return result


def part_two(positions, depth_matrix):
    basins = []
    for position in positions:
        basins.append(flood(position, depth_matrix, []))
    basins.sort()
    print(basins)
    print(basins[-3] * basins[-2] * basins[-1])


def main():
    lines = read_file("input.txt")
    depth_matrix = [list(map(int, str(line))) for line in lines]
    positions = part_one(depth_matrix)
    part_two(positions, depth_matrix)


main()
