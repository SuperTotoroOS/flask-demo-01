# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys

def is_valid(word, arity):
    is_char = False
    flag = ''
    for i in word:
        if i.isalpha and is_char != True:
            is_char = True
            flag = flag + 'x'
            if flag == 'x_x' or flag == 'x.x_x':
                break
        elif i == ' ' and is_char != False:
            is_char = False
            flag = flag + '_'
            if flag == 'x_x' or flag == 'x.x_x':
                break
        elif i in ',()':
            is_char = False
            flag = flag + '.'
            if flag == 'x_x' or flag == 'x.x_x':
                break
        else:
            continue
    if flag == 'x_x' or flag == 'x.x_x':
        return False

    is_char = False
    word_list = []
    for i in word:
        if i == ' ':
            continue
        if i in ',()':
            word_list.append(i)
            is_char = False
        elif not i.isalpha() and i != '_':
            return False
        elif not is_char:
            is_char = True
            word_list.append('x')
    word = ''.join(word_list)

    if arity == 0:
        return word == 'x'
    if arity > 1 and word == 'x':
        return False
    else:
        pattern = 'x(' + 'x,' * (arity - 1) + 'x)'
        while True:
            handled_word = word.replace(pattern, 'x')
            if handled_word == word:
                break
            word = handled_word
        return word == 'x'
    
try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')

