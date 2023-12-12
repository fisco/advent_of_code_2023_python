import copy
import networkx as nx

matrix = []
directional_characters = {'←', '↑', '→', '↓'}
extremes = {}


def can_walk_out(row, column):
    # Easy cases:
    # north
    for r in range(row, -2, -1):
        if r == -1:
            return True
        if matrix[r][column] in directional_characters:
            break
    # south
    for r in range(row, len(matrix)+1):
        if r == len(matrix):
            return True
        if matrix[r][column] in directional_characters:
            break
    # east
    for c in range(column, len(matrix[row])+1):
        if c == len(matrix[row]):
            return True
        if matrix[row][c] in directional_characters:
            break
    # west
    for c in range(column, -2, -1):
        if c == -1:
            return True
        if matrix[row][c] in directional_characters:
            break

    return False

def find_first_cell_to_take(current_array_number, current_index):
    if current_index - 1 >= 0:
        if matrix[current_array_number][current_index-1] in {'-', 'L', 'F'}:
            return(current_array_number, current_index-1)
    if current_index + 1 < len(matrix[current_array_number]):
        if matrix[current_array_number][current_index+1] in {'-', 'J', '7'}:
            return(current_array_number, current_index+1)
    if current_array_number - 1 >=0:
        if matrix[current_array_number-1][current_index] in {'|', 'F', '7'}:
            return(current_array_number-1, current_index)
    if current_array_number + 1 < len(matrix[current_array_number]):
        if matrix[current_array_number+1][current_index] in {'|', 'J', 'L'}:
            return(current_array_number+1, current_index)
    return None

with open('input.txt', 'r') as f:
    for index, line in enumerate(f):
        matrix.append(list(line.strip()))

stashed_matrix = copy.deepcopy(matrix)

target_char = 'S'
starting_row_index = None
starting_array_index = None
for i, inner_array in enumerate(matrix):
    for j, char in enumerate(inner_array):
        if char == target_char:
            starting_row_index = i
            starting_array_index = j
            break

# matrix[starting_row_index][starting_array_index] = 'X'
cell_tuple = find_first_cell_to_take(starting_row_index, starting_array_index)
array_number = cell_tuple[0]
column_number = cell_tuple[1]

# READ cell
# if S, you are finished
# determine two possible paths
# mark cell as X
# take determined path that doesn't match X
visited = []
counter = 1
while (starting_row_index != array_number) or (starting_array_index != column_number):
    direction = matrix[array_number][column_number]
    visited.append((array_number, column_number))
    # matrix[array_number][column_number] = 'X'
    match direction:
        case '|': #is a vertical pipe connecting north and south.
            if matrix[array_number-1][column_number] not in directional_characters:
                matrix[array_number][column_number] = '↑'
                array_number -= 1
            else:
                matrix[array_number][column_number] = '↓'
                array_number += 1
        case '-': #is a horizontal pipe connecting east and west.
            if matrix[array_number][column_number-1] not in directional_characters:
                matrix[array_number][column_number] = '←'
                column_number -= 1
            else:
                matrix[array_number][column_number] = '→'
                column_number += 1
        case 'L': #is a 90-degree bend connecting north and east.
            if matrix[array_number-1][column_number] not in directional_characters:
                matrix[array_number][column_number] = '↑'
                array_number -= 1
            else:
                matrix[array_number][column_number] = '→'
                column_number += 1
        case 'J': #is a 90-degree bend connecting north and west.
            if matrix[array_number-1][column_number] not in directional_characters:
                matrix[array_number][column_number] = '↑'
                array_number -= 1
            else:
                matrix[array_number][column_number] = '←'
                column_number -= 1
        case '7': #is a 90-degree bend connecting south and west.
            if matrix[array_number][column_number-1] not in directional_characters:
                matrix[array_number][column_number] = '←'
                column_number -= 1
            else:
                matrix[array_number][column_number] = '↓'
                array_number += 1
        case 'F': #is a 90-degree bend connecting south and east.
            if matrix[array_number][column_number+1] not in directional_characters:
                matrix[array_number][column_number] = '→'
                column_number += 1
            else:
                matrix[array_number][column_number] = '↓'
                array_number += 1
        case _:
            print("Major problem. The value is: " + direction)
    counter += 1

print("---")
print("In part 1, steps it takes along the loop to get from the starting position to the point farthest from the starting position is " + str(counter/2))



for i, row in enumerate(matrix):
    for j, column in enumerate(row):
        if column not in directional_characters:
            if can_walk_out(i, j):
                matrix[i][j] = 'O'


#print(matrix[21][93])
#print(can_walk_out(21, 93))

#for each in visited:
#    print(each)
#print(f"Has duplicates: {len(visited) != len(set(visited))}")

#find_the_extremes(matrix)

#strings = list(map(lambda sub_array: ''.join(sub_array), matrix))
#for string in strings:
#    print(string)

# You close a loop when you encounter the path next to you, but progress in the opposite direction of the formerly walked path.
# So, as you create the path, keep paired nodes_of_closure
# Then walk each one backwards, marking the Is 
# A looped area cannot have any tunnels in it.

#def find_the_extremes(m):
#    for i, r in enumerate(m):
#        # Look for right-hand turn
#        for j, c in enumerate(r):
#            if c == '→' and m[i+1][j] == '↑':
#                m[i][j] = 'B'

# Every time you take a turn, check the direction in which you were going.
# If you were heading east or west, if you brush against something heading north or south, you closed a loop. Zap in opposite N-S direction.
# If you were heading north or south, if you brush against something heading east or west, you closed a loop.  Zap in opposite E-W direction.

# When you take a turn, if there is a block ahead of the turn that was | or - you have closed a loop.
# 
# At every L and every F, see if there is an unbroken box.
#   

target_char = 'S'
starting_row_index = None
starting_array_index = None
for i, inner_array in enumerate(stashed_matrix):
    for j, char in enumerate(inner_array):
        if char == target_char:
            starting_row_index = i
            starting_array_index = j
            stashed_matrix[starting_array_index][starting_row_index] = 'B'
            break


while (starting_row_index != array_number) or (starting_array_index != column_number):
    direction = stashed_matrix[array_number][column_number]
    visited.append((array_number, column_number))
    # stashed_matrix[array_number][column_number] = 'X'
    match direction:
        case '|': #is a vertical pipe connecting north and south.
            if stashed_matrix[array_number-1][column_number] not in directional_characters:
                stashed_matrix[array_number][column_number] = 'N'
                array_number -= 1
            else:
                stashed_matrix[array_number][column_number] = 'S'
                array_number += 1
        case '-': #is a horizontal pipe connecting east and west.
            if stashed_matrix[array_number][column_number-1] not in directional_characters:
                stashed_matrix[array_number][column_number] = 'W'
                column_number -= 1
            else:
                stashed_matrix[array_number][column_number] = 'E'
                column_number += 1
        case 'L': #is a 90-degree bend connecting north and east.
            if stashed_matrix[array_number-1][column_number] not in directional_characters:
                stashed_matrix[array_number][column_number] = 'N'
                array_number -= 1
            else:
                stashed_matrix[array_number][column_number] = 'E'
                column_number += 1
        case 'J': #is a 90-degree bend connecting north and west.
            if stashed_matrix[array_number-1][column_number] not in directional_characters:
                stashed_matrix[array_number][column_number] = 'N'
                array_number -= 1
            else:
                stashed_matrix[array_number][column_number] = 'W'
                column_number -= 1
        case '7': #is a 90-degree bend connecting south and west.
            if stashed_matrix[array_number][column_number-1] not in directional_characters:
                stashed_matrix[array_number][column_number] = 'W'
                column_number -= 1
            else:
                stashed_matrix[array_number][column_number] = 'S'
                array_number += 1
        case 'F': #is a 90-degree bend connecting south and east.
            if stashed_matrix[array_number][column_number+1] not in directional_characters:
                stashed_matrix[array_number][column_number] = 'E'
                column_number += 1
            else:
                stashed_matrix[array_number][column_number] = 'S'
                array_number += 1
        case _:
            print("Major problem. The value is: " + direction)
    counter += 1



G = nx.DiGraph()

# Add nodes and edges based on the stashed_matrix
for i in range(len(stashed_matrix)):
    for j in range(len(stashed_matrix[i])):
        G.add_node((i, j))  # Add node with coordinates
        # Check for valid connections
        if i > 0 and stashed_matrix[i-1][j] != "S":
            G.add_edge((i, j), (i-1, j), weight=stashed_matrix[i-1][j])
        if j < len(stashed_matrix[i])-1 and stashed_matrix[i][j+1] != "W":
            G.add_edge((i, j), (i, j+1), weight=stashed_matrix[i][j+1])
        if i < len(stashed_matrix)-1 and stashed_matrix[i+1][j] != "N":
            G.add_edge((i, j), (i+1, j), weight=stashed_matrix[i+1][j])
        if j > 0 and stashed_matrix[i][j-1] != "E":
            G.add_edge((i, j), (i, j-1), weight=stashed_matrix[i][j-1])




strings = list(map(lambda sub_array: ''.join(sub_array), stashed_matrix))
for string in strings:
    print(string)

