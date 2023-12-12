from collections import deque
from heapq import heappop, heappush
#import networkx as nx
import numpy as np
import pprint
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from scipy import sparse

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

#for r in matrix:
#    print(''.join(r))

all_pairs = []
for i in range(1, max_node_number+1):
    for j in range(i, max_node_number+1):
       if i != j:
           all_pairs.append((i, j))
#print(all_pairs)

total = 0
#for p in all_pairs:
#   print(p[0])
#   total += shortest_distance(matrix, find_address(matrix, p[0]), find_address(matrix, p[1]))

#print("For part 1, the total number of shortest distances is " + str(total))
print("For part 1, the total number of shortest distances is " + str(9521776))

# Now, attempt a sparse matrix for part 2
# Now, attempt a sparse matrix for part 2
# Now, attempt a sparse matrix for part 2

# Create matrix with periods changed to None

matrix = []

counter = 1
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        characters = []
        for c in line.strip():
            if c == '#':
              c = int(counter)
              counter += 1
            else:
              c = 0
            characters.append(c)
        matrix.append(characters)
max_node_number = counter -1

#print(matrix)

# Make it sparse and expand it
# Assuming your matrix is called "matrix"
if isinstance(matrix, list):
  matrix = np.array(matrix)  # Convert list of lists to NumPy array
  empty_row = np.zeros(len(matrix[0]))  # Create an empty row
  sparse_matrix = csr_matrix(matrix)  # Convert the matrix to sparse format
else:
  empty_row = np.zeros(matrix.shape[1])  # Create an empty row
  sparse_matrix = csr_matrix(matrix)  # Convert the matrix to sparse format

# Find all rows with only zeros
zero_rows = np.where(np.all(matrix == 0, axis=1))[0]

# Create arrays for empty rows
empty_rows = np.repeat(zero_rows + 1, 1000000, axis=0)
empty_data = np.zeros(len(empty_rows))

# Convert to COO format for manipulation
sparse_matrix = sparse_matrix.tocoo()

# Combine data and indices
combined_row = np.concatenate((sparse_matrix.row, empty_rows))
combined_col = np.concatenate((sparse_matrix.col, empty_data))
combined_data = np.concatenate((sparse_matrix.data, np.zeros(len(empty_rows))))

# Ensure consistent order of rows and columns
sorted_indices = np.lexsort((combined_row, combined_col))
combined_row = combined_row[sorted_indices]
combined_col = combined_col[sorted_indices]
combined_data = combined_data[sorted_indices]

# Convert back to CSR format
sparse_matrix = csr_matrix((combined_data, (combined_row, combined_col)), shape=(matrix.shape[0] + len(zero_rows) * 1000000, matrix.shape[1]))

# make it u16
# Convert to u16
sparse_matrix = sparse_matrix.astype(np.uint16)

# NOW ADD THE MILLIONS OF columns

# Check if sparse_matrix is a csr_matrix
if not isinstance(sparse_matrix, csr_matrix):
    raise TypeError("sparse_matrix must be a csr_matrix")

# Get indices of columns with only zeros or empty elements
zero_cols = np.where(np.all(sparse_matrix.data == 0, axis=0))[0]

# Get indices of non-zero columns
nonzero_cols = np.setdiff1d(np.arange(sparse_matrix.shape[1]), zero_cols)

# Create a new empty matrix with one million columns
empty_cols = np.empty((sparse_matrix.shape[0], 1000000), dtype=sparse_matrix.dtype)

# Combine the non-zero and empty columns
combined_matrix = csr_matrix(
    np.concatenate((sparse_matrix[:, nonzero_cols].toarray(), empty_cols), axis=1),
    shape=(sparse_matrix.shape[0], 1000000 + len(nonzero_cols)),
)

# Update sparse_matrix
sparse_matrix = combined_matrix


'''
matrix_sparse = sparse.csr_matrix(matrix)

print(f"Shape of the sparse matrix: {matrix_sparse.shape}")
matrix_coo = matrix_sparse.tocoo()
for i, (row, col, val) in enumerate(zip(matrix_coo.row, matrix_coo.col, matrix_coo.data)):
    print(f"Element at row {row}, column {col}: {val}")

# Check if the matrix is empty
if not matrix_sparse.size:
    # Create an empty sparse matrix with desired dimensions
    empty_matrix = sparse.lil_matrix((1000000, 1000000), dtype=matrix_sparse.dtype)
else:
    # Identify rows and columns with only zeros
    matrix_sparse = matrix_sparse.tocsc()
    all_zeros_rows = np.where(np.all(matrix_sparse == 0, axis=1))[0]
    matrix_sparse = matrix_sparse.tocsr()
    all_zeros_cols = np.where(np.all(matrix_sparse == 0, axis=0))[1]

    # Create empty rows and columns
    empty_rows = sparse.lil_matrix((1000000 - len(all_zeros_rows), matrix_sparse.shape[1]), dtype=matrix_sparse.dtype)
    empty_cols = sparse.lil_matrix((matrix_sparse.shape[0], 1000000 - len(all_zeros_cols)), dtype=matrix_sparse.dtype)

    # Combine sparse matrices
    matrix_sparse = sparse.vstack([matrix_sparse, empty_rows])
    matrix_sparse = sparse.hstack([matrix_sparse, empty_cols])

    # Update row and column indices
    row_indices = np.arange(matrix_sparse.shape[0])
    col_indices = np.arange(matrix_sparse.shape[1])
    row_indices[all_zeros_rows] = np.arange(matrix_sparse.shape[0] - len(all_zeros_rows))
    col_indices[all_zeros_cols] = np.arange(matrix_sparse.shape[1] - len(all_zeros_cols))

    # Convert to the desired format
    matrix_sparse = matrix_sparse[row_indices, :]
    matrix_sparse = matrix_sparse[:, col_indices]

'''
