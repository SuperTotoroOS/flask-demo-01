import sys
import re


class Error(Exception):
    pass


class InputError(Error):
    pass


class ConvertFormatError(Error):
    pass


romanNumberDict = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                   ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                   ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))

romanNumberPattern = r"^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"


def converter(value):
    if value.isdigit():
        result = ''
        int_value = int(value)
        if not 0 < int_value < 4000 and int_value == value:
            raise ConvertFormatError()
        for roman, num in romanNumberDict:
            while int_value >= num:
                result += roman
                int_value -= num
        return result
    elif value.isalpha():
        if not re.search(romanNumberPattern, value):
            raise ConvertFormatError()
        result = 0
        index = 0
        for roman, num in romanNumberDict:
            while value[index:index + len(roman)] == roman:
                result += num
                index += len(roman)
        arabic = str(result)
        return arabic
    else:
        raise ConvertFormatError()


def converter_by_distinct(value1, value2):
    if value1.isdigit():
        result = ''
        int_value = int(value)
        if not 0 < int_value and int_value == value:
            raise ConvertFormatError()
    elif value1.isalpha():
        if len(set(value2)) != len(value2):
            raise ConvertFormatError()


try:
    input_value = input('How can I help you? ')
    print(input_value)
    if not input_value.startswith('Please convert'):
        raise InputError()

    split_str = input_value.split(' ')
    if len(split_str) == 3:
        value = split_str[2]
        result = converter(value)
        print('Sure! It is ' + result)
    elif len(split_str) == 5:
        value1 = split_str[2]
        value2 = split_str[4]
        result = converter_by_distinct(value1, value2)
        # print('Sure! It is ' + result)
    elif len(split_str) == 4:
        pass
except InputError:
    print('I don\'t get what you want, sorry mate!')
    sys.exit()
except ConvertFormatError:
    print('Hey, ask me something that\'s not impossible to do!')
    sys.exit()
