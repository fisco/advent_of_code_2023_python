import numpy as np
import re
from itertools import cycle

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

''' def gcd(a, b):
    if b == 0:
        return a
    else:
        gcd(b, a % b)

def lcm(numbers):
    lcm = 1
    for number in numbers:
        print(type(lcm))
        print(type(number))
        lcm = (lcm * number) / gcd(lcm, number)
    return lcm
    '''

def lcm(numbers):
    if len(numbers) == 2:
        return np.lcm(numbers[0], numbers[1])
    else:
        return np.lcm(numbers[0], lcm(numbers[1:]))


node_map = {}
with open('input.txt', 'r') as f:
    for index, line in enumerate(f):
        if index == 0:
            loop_string = line.strip()
        if index > 1:
            split_on_equal = line.strip().split(" = ")
            left_and_right = split_on_equal[1].split(", ")
            node = Node(left_and_right[0].replace('(', ''), left_and_right[1].replace(')', ''))
            node_map[split_on_equal[0]] = node

node_to_consider  = "AAA"
leaps = 0
for character in cycle(loop_string):
    if node_to_consider == "ZZZ":
        break
    else:
        next_location_possibilities = node_map[node_to_consider]
        if character == 'R':
            node_to_consider = next_location_possibilities.right
        else:
            node_to_consider = next_location_possibilities.left
        leaps += 1

print("In part 1, the steps required to reach ZZZ total " + str(leaps))

keys = list(node_map.keys())
group_of_nodes = list(filter(lambda string: re.match(r"..A", string), keys))
shortest_paths = []
for n in group_of_nodes:
    leaps = 0;
    node_to_consider = n
    for character in cycle(loop_string):
        if re.match(r"..Z", node_to_consider):
            break;
        else:
            next_location_possibilities = node_map[node_to_consider]
            if character == 'R':
                node_to_consider = next_location_possibilities.right
            else:
                node_to_consider = next_location_possibilities.left
        leaps += 1
    shortest_paths.append(leaps)

#print(shortest_paths)

print("The number of steps it takes before you're only on nodes that end with Z: " + str(lcm(shortest_paths)))
