from itertools import cycle

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def gcd(a, b):
    if b == 0:
        return a
    else:
        gcd(b, a % b)

def lcm(numbers):
    lcm = 1
    for number in numbers:
        lcm = lcm * (number) / gcd(lcm, number)
    return lcm

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

