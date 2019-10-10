# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
for k, v in mapping.items():
    sub_cycles = []
    while v in mapping.keys():
        if len(sub_cycles) > len(mapping.keys()):
            break
        sub_cycles.append(v)
        sub_cycles.append(mapping[v])
        v = mapping[v]
        if sub_cycles[0] == sub_cycles[-1]:
            temp_list = sorted(set(sub_cycles))
            if temp_list not in cycles:
                cycles.append(temp_list)
            break

values_set = set()
for k, v in mapping.items():
    values_set.add(v)

for i in values_set:
    keys_list = []
    for k, v in mapping.items():
        if v == i:
            keys_list.append(k)
    # print(i, keys_list)
    if len(keys_list) not in reversed_dict_per_length.keys():
        reversed_dict_per_length[len(keys_list)] = {i: keys_list}
    else:
        reversed_dict_per_length[len(keys_list)][i] = keys_list


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


