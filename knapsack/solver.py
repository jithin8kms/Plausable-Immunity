
#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    n_array = [[0 for w in range(capacity + 1)] for i in range(item_count + 1)]

    for i, item in enumerate(items):
        i += 1
        for w in range(1, capacity + 1):
            if item.weight <= w:
                n_array[i][w] = max(n_array[i - 1][w - item.weight] + item.value, n_array[i - 1][w])
            else:
                n_array[i][w] = n_array[i - 1][w]

    taken = [0] * item_count

    index = capacity
    
    for array_index in reversed(range(0, item_count + 1)):
        
        if n_array[array_index][index] != n_array[array_index - 1][index]:
            taken[array_index - 1] = 1
            index = index - items[array_index - 1].weight
        

# =============================================================================
#     def rec_fun(index, array_index):
#         if array_index == 0:
#             return
#         if n_array[array_index][index] != n_array[array_index - 1][index]:
#             taken[array_index - 1] = 1
#             index = index - items[array_index - 1].weight
#         array_index = array_index - 1
#         rec_fun(index, array_index)
# 
#     rec_fun(capacity, item_count)
# 
# =============================================================================
    # prepare the solution in the specified output format
    output_data = str(n_array[-1][-1]) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
