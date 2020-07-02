from collections import OrderedDict


class RomanNumerals:
    """
    This implementation of RomanNumerals has been made without a constructor and the use
    """
    rom_dict = OrderedDict([('*', 0), ('I', 1), ('V', 5), ('X', 10), ('L', 50),
                            ('C', 100), ('D', 500), ('M', 1000)])

    def to_roman(value=None):
        rev_list = [int(i) for i in str(value)[::-1]]
        result_list = [
            RomanNumerals.roman_str_gen(int(val), idx)
            for idx, val in enumerate(rev_list)
        ]
        string = ''.join(result_list[::-1]).replace('*', '')
        return string

    def from_roman(string):
        val = prev = 0
        for char in string[::-1]:
            cur = RomanNumerals.rom_dict[char]
            if prev > cur:
                val -= cur
            else:
                val += cur
            prev = cur

        return val

    def roman_str_gen(value=0, power=0, base=10):

        digit_place = base**power
        val = int(value) * digit_place
        upper = lower = 'I'
        roman_string = ''

        # Takes care of cases where the value is 0 or already present
        if RomanNumerals.get_key(val):
            return RomanNumerals.get_key(val)

        # Find the boundary for the value observed
        for k, v in RomanNumerals.rom_dict.items():
            if v >= val:
                lower, upper = upper, k
                break
            lower = upper = k

        # Find starting value to generate numeral string
        if abs(RomanNumerals.rom_dict[upper] - val) <= digit_place:
            roman_string = RomanNumerals.subtract_val(val, upper)
        else:
            roman_string = RomanNumerals.add_val(val, lower)

        return roman_string

    def add_val(target=0, start='', base=10):
        is_match = False
        power = repeat = 0
        test_string = f'{start}{RomanNumerals.get_key(base**power)*repeat}'

        while is_match == False:
            if RomanNumerals.from_roman(test_string) == target:
                is_match = True
            elif RomanNumerals.from_roman(
                    test_string) != target and repeat >= 3:
                power += 1
                repeat = 0
            else:
                repeat += 1
            test_string = f'{start}{RomanNumerals.get_key(base**power)*repeat}'
        return test_string

    def subtract_val(target=0, start='', base=10):
        is_match = False
        power = 0
        while is_match == False:
            test_string = f'{RomanNumerals.get_key(base**power)}{start}'
            if RomanNumerals.from_roman(test_string) == target:
                is_match = True
            power += 1
        return test_string

    def get_key(val):
        for key, value in RomanNumerals.rom_dict.items():
            if val == value:
                return key
        return False
