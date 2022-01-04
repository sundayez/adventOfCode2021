def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []  # of type Node

    def add_adjacent(self, node):
        self.adjacent.append(node)


class RuleGraph:
    def __init__(self, root):
        self.node_map = {root.value: root}
        self.root = root

    def add_rule(self, rule):
        node_left, node_right = build_nodes_from_rule(rule)
        if rule[0] not in self.node_map:
            self.node_map[rule[0]] = node_left
        else:
            if rule[1] not in self.node_map:
                self.node_map[rule[0]].adjacent.add(node_right)
                self.node_map[rule[1]].adjacent.add(node_left)
            #else:


def build_nodes_from_rule(rule):
    node_left = Node(rule[0])
    node_right = Node(rule[1])
    node_left.add_adjacent(node_right)
    node_right.add_adjacent(node_left)
    return node_left, node_right


def build_graph(rules):
    node_left, node_right = build_nodes_from_rule(rules[0])
    graph = RuleGraph(node_left)
    return graph


def part_one(graph):
    print(graph.root.value)
    print(graph.root.adjacent[0].value)
    print(graph.root.adjacent[0].adjacent[0].value)


def part_two(graph):
    return 0


def main():
    lines = read_file("input.txt")
    rules = [line.split('-') for line in lines]
    print(rules)
    graph = build_graph(rules)
    part_one(graph)
    part_two(graph)


main()
