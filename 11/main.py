from collections import deque
from heapq import heappop, heappush
import networkx as nx
import numpy as np
import pprint
from scipy.sparse import csr_matrix, csc_matrix


def find_address(matrix, number):
  """
  Finds the row and column index of a number in a matrix.

  Args:
    matrix: A nested array of strings and unique numbers.
    number: The number to find.

  Returns:
    A tuple (row, column) if the number is found, else None.
  """
  for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
      if (element != '.') and element == str(number):
        return row_index, col_index
  return None

def shortest_distance(matrix, start, end):
  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  distances = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
  distances[start] = 0
  pq = [(0, start)]

  while pq:
    current_distance, current_cell = heappop(pq)
    visited.add(current_cell)

    if current_cell == end:
      return current_distance

    for neighbor in [(current_cell[0] + 1, current_cell[1]), (current_cell[0] - 1, current_cell[1]),
                      (current_cell[0], current_cell[1] + 1), (current_cell[0], current_cell[1] - 1)]:
      if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in visited:
        new_distance = current_distance + 1
        if new_distance < distances[neighbor]:
          distances[neighbor] = new_distance
          heappush(pq, (new_distance, neighbor))

  return -1

## BEGIN WORK

matrix = []

# Create matrix with doubled blank rows
counter = 1
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        characters = []
        for c in line.strip():
            if c == '#':
                c = int(counter)
                counter += 1
            characters.append(c)
        matrix.append(characters)
        if all(x == characters[0] for x in characters):
            matrix.append(characters)
max_node_number = counter -1

# Double the blank columns in matrix
inverted_matrix = np.transpose(matrix)
matrix = []
for r in inverted_matrix:
    matrix.append(r)
    if all(x == r[0] for x in r):
        matrix.append(r)
matrix = np.transpose(matrix)

# Convert numpy matrix to ordinary matrix
matrix = matrix.tolist()

for r in matrix:
    #for c in r:
    #   print(isinstance(c, int))
    print(''.join(r))

all_pairs = []
for i in range(1, max_node_number+1):
    for j in range(i, max_node_number+1):
       if i != j:
           all_pairs.append((i, j))
#print(all_pairs)

total = 0
for p in all_pairs:
   print(p[0])
   total += shortest_distance(matrix, find_address(matrix, p[0]), find_address(matrix, p[1]))

#print("For part 1, the total number of shortest distances is " + str(total))
print("For part 1, the total number of shortest distances is " + str(9521776))
print("For part 1, the total number of shortest distances is " + str(total))


# Now, attempt a sparse matrix for part 2
