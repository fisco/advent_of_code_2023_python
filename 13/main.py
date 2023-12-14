import numpy as np
import sys

class Pattern:
  def __init__(self, matrix):
    self.matrix = np.array(matrix)

  def count_matrix_reflecting_lines(m):
    for i in range(1, len(m)):
      top_part = m[:i]
      bottom_part = m[i:]
      if len(top_part) > len(bottom_part):
        top_part = top_part[(len(top_part) - len(bottom_part)):]
      if len(bottom_part) > len(top_part):
        bottom_part = bottom_part[:-(len(bottom_part) - len(top_part))]
      if np.array_equal(top_part[::-1], bottom_part):
        return i
    return 0

  def summary(self):
    c = Pattern.count_matrix_reflecting_lines(self.matrix)
    if c > 0:
      print(self.matrix)
      print(c)
      return c*100
    else:
      # Transpose the matrix
      transposed_matrix = np.transpose(self.matrix)
      # Rearrange the elements based on the desired pattern
      # reshaped_matrix = transposed_matrix[::-1]
      print(transposed_matrix)
      print(str(Pattern.count_matrix_reflecting_lines(transposed_matrix)))
      return Pattern.count_matrix_reflecting_lines(transposed_matrix)

patterns = []

with open('input.txt', 'r') as f:
  arrays = []
  for line in f:
    print(line)
    s = line.strip()
    if len(s) > 0:
      array = []
      for c in s:
        array.append(c)
      arrays.append(array)
    else:
      patterns.append(Pattern(arrays))
      arrays = []

#return_values = [p.summary() for p in patterns]
#[print(p.matrix) for p in patterns ]
print("Number after summarizing all notes: " + str(sum([p.summary() for p in patterns])))
