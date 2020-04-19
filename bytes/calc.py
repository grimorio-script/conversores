#!/usr/bin/python3
import sys
from math import floor, log, pow


def convert_size(num_bytes, size='B'):
    converted_bytes = calculate_byte(num_bytes)
    byte_letter = return_name_tag(num_bytes, size)
    return f'{converted_bytes} {byte_letter}'


def calculate_byte(num):
    base = return_byte_base()
    num_logaritm = int(floor(return_log(num, base)))
    product = pow(base, num_logaritm)
    result = round(num / product, 2)
    if num < base or result in reference_index():
        return int(result)
    else:
        return result


def return_byte_base():
    return 1024


def return_log(num1, num2):
    if num1 <= 0:
        print('Negative number error.')
        quit()
    else:
        return log(num1, num2)


def return_name_tag(num, choice='B'):
    byte_unit = byte_reference(choice.upper())
    base = return_byte_base()
    position = int(floor(return_log(num, base)))
    return byte_unit[position]


def byte_reference(index='B', short=True):
    if index in byte_units() and short is True:
        return return_abbreviated(index)
    elif index in long_byte_units() and short is False:
        return return_full_unit_name(index)
    else:
        return f'{index} is an invalid value.'


def byte_units():
    units = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    return units


def return_abbreviated(index):
    abbreviated = byte_units().index(index)
    return byte_units()[abbreviated:]


def return_full_unit_name(index):
    full_name = long_byte_units()[index]
    return full_name


def long_byte_units():
    units = {'B': 'Byte', 'KB': 'KiloByte', 'MB': 'MegaByte', 'GB': 'GygaByte', 'TB': 'TeraByte',
             'PB': 'PetaByte', 'EB': 'ExaByte', 'ZB': 'ZetaByte', 'YB': 'YottaByte'}
    return units


def reference_index():
    indexes = [count for count in range(0, len(byte_reference()))]
    return indexes


def commandline():
    try:
        arg = int(sys.argv[1])
    except IndexError:
        print('This program must be executed from command-line\n'
              'usage: byteconvert [int]')
    except ValueError:
        arg = sys.argv[1]
        print(f"'{arg}' its not a number, so it cannot be converted into bytes.")
    else:
        converted_value = convert_size(arg)
        print(converted_value)


if __name__ == '__main__':
    commandline()
