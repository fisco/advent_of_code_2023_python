from functools import reduce
import re

total = 0
gear_ratio_total = 0
file_array = []

with open('input.txt', 'r') as f:
    for line in f:
        file_array.append(line.strip())
line_length = len(file_array[0])

for index, line in enumerate(file_array):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        window_column_start = max(match.start() - 1, 0)
        window_column_end = min(match.end() + 1, line_length)
        test_string = ""
        for row_window in range(max(index-1, 0), min(index+2, len(file_array)-1)):
            test_string += file_array[row_window][window_column_start:window_column_end]
        if len(re.sub(r"[\d\.]+", "", test_string)) > 0:
            total += int(match.group())


for index, line in enumerate(file_array):
    for i, c in enumerate(line):
        if c == '*':
            window_column_start = max(i - 1, 0)
            window_column_end = min(i + 1, line_length)
            potential_gears = []
            for row_window in range(max(index-1, 0), min(index+2, len(file_array))):
                matches = re.finditer(r"[0-9]+", file_array[row_window])
                for match in matches:
                    if bool(set(range(window_column_start, window_column_end+1))
                          .intersection(set(range(match.start(), match.end())))):
                        potential_gears.append(match.group())
            if len(potential_gears) > 1:
                gear_ratio_total += reduce(lambda x, y: x * y, map(int, filter(None, map(int, potential_gears))))
        
print("The sum of the part numbers is: " + str(total))
print("The sum of all gear ratios is: " + str(gear_ratio_total))
