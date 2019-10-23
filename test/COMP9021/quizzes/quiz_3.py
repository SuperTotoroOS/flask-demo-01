# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.')
print()

# INSERT YOUR CODE HERE
converted_list = list('0' * nb_of_leading_zeroes + str('{0:o}'.format(int(code))))[::-1]

current_row = 0
current_col = 0

path = []

row_list = []
col_list = []


def move(a, b):
    step = [a, b]
    if step in path:
        path.remove(step)
    else:
        path.append(step)
    return path


for i in converted_list:
    # 北
    if i == '0':
        current_row -= 1
        move(current_row, current_col)
    # 东北
    elif i == '1':
        current_row -= 1
        current_col += 1
        move(current_row, current_col)
    # 东
    elif i == '2':
        current_col += 1
        move(current_row, current_col)
    # 东南
    elif i == '3':
        current_row += 1
        current_col += 1
        move(current_row, current_col)
    # 南
    elif i == '4':
        current_row += 1
        move(current_row, current_col)
    # 西南
    elif i == '5':
        current_row += 1
        current_col -= 1
        move(current_row, current_col)
    # 西
    elif i == '6':
        current_col -= 1
        move(current_row, current_col)
    # 西北
    elif i == '7':
        current_row -= 1
        current_col -= 1
        move(current_row, current_col)

path.append([0, 0])

for i in path:
    row = i[0]
    col = i[1]
    row_list.append(row)
    col_list.append(col)

if path:
    min_row = min(row_list)
    min_col = min(col_list)

    max_row = max(row_list)
    max_col = max(col_list)

    num_row = max_row - min_row + 1
    num_col = max_col - min_col + 1

    if min_row < 0:
        for i in path:
            i[0] += abs(min_row)
    elif min_row > 0:
        for i in path:
            i[0] -= min_row

    if min_col < 0:
        for i in path:
            i[1] += abs(min_col)
    elif min_col > 0:
        for i in path:
            i[1] -= min_col

    graph = []

    for i in range(num_row):
        graph.append([])
        for j in range(num_col):
            if [i, j] in path:
                graph[i].append(on)
            else:
                graph[i].append(off)

    for i in graph:
        for j in i:
            print(j, end='')
        print()
