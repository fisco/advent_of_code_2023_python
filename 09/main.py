with open('input.txt', 'r') as f:
    next_number_total = 0
    earlier_number_total = 0
    for index, line in enumerate(f):
        iterated_arrays = []
        current_array = [int(x) for x in line.strip().split(" ")]
        next_number = current_array[-1]
        earlier_number_multiplier = 1
        earlier_number = current_array[0] * earlier_number_multiplier
        while any(current_array):
            earlier_number_multiplier *= -1
            current_array = [current_array[i + 1] - current_array[i] for i in range(len(current_array) - 1)]
            next_number += current_array[-1]
            earlier_number += current_array[0] * earlier_number_multiplier
        next_number_total += next_number
        earlier_number_total += earlier_number

print("In part 1, the the sum of the extrapolated values is " + str(next_number_total))
print("In part 2, the sum of the earlier extrapolated values is " + str(earlier_number_total))
