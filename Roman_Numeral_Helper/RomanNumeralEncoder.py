from collections import OrderedDict
"""
Codidng challeng @ https://www.codewars.com/kata/51b62bf6a9c58071c600001b
"""

def solution(n):
    # TODO convert int to roman string
    rom_dict = OrderedDict([('*', 0), ('I', 1), ('V', 5), ('X', 10), ('L', 50),
                            ('C', 100), ('D', 500), ('M', 1000)])
    rev_list = [int(i) for i in str(n)[::-1]]
    result_list = []
    for idx, val in enumerate(rev_list):
        r = roman_str_gen(rom_dict, val, idx)
        result_list.append(r)
    string = ''.join(result_list[::-1]).replace('*', '')
    return string


def from_roman(rom_dict=None, string=''):
    val = prev = 0
    for char in string[::-1]:
        cur = rom_dict[char]
        if prev > cur:
            val -= cur
        else:
            val += cur
        prev = cur
    return val


def roman_str_gen(rom_dict=None, value=0, power=0, base=10):
    # Takes care of cases where the value is 0 or already present
    digit_place = base**power
    val = int(value) * digit_place
    upper = lower = 'I'
    roman_string = ''

    key = get_key(rom_dict, val)
    if key:
        return key

    # Find the boundary for the value observed
    for k, v in rom_dict.items():
        if v >= val:
            lower, upper = upper, k
            break
        lower = upper = k

    # Find starting value to generate numeral string
    if abs(rom_dict[upper] - val) <= digit_place:
        roman_string = subtract_val(rom_dict, val, upper)
    else:
        roman_string = add_val(rom_dict, val, lower)

    return roman_string


def get_key(rom_dict=None, val=None):
    for key, value in rom_dict.items():
        if val == value:
            return key
    return False


def add_val(rom_dict=None, target=0, start='', base=10):
    is_match = False
    power = repeat = 0
    test_string = f'{start}{get_key(rom_dict, base**power)*repeat}'

    while is_match == False:
        if from_roman(rom_dict, test_string) == target:
            is_match = True
        elif from_roman(rom_dict, test_string) != target and repeat >= 3:
            power += 1
            repeat = 0
        else:
            repeat += 1
            test_string = f'{start}{get_key(rom_dict, base**power)*repeat}'
    return test_string


def subtract_val(rom_dict=None, target=0, start='', base=10):
    is_match = False
    power = 0
    while is_match == False:
        test_string = f'{get_key(rom_dict, base**power)}{start}'
        if from_roman(rom_dict, test_string) == target:
            is_match = True
        power += 1
    return test_string
