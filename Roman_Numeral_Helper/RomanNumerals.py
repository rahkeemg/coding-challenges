from collections import OrderedDict


class RomanNumerals:
    def __init__(self):
        """
          Constructor
        """
        self.rom_dict = OrderedDict([('*', 0), ('I', 1), ('V', 5), ('X', 10),
                                     ('L', 50), ('C', 100), ('D', 500),
                                     ('M', 1000)])

    def to_roman(self, value=0):
        """
          Converts a number into its roman numeral representation as a string
        """
        rev_list = [int(i) for i in str(value)[::-1]]
        result_list = [
            self.roman_str_gen(val, idx) for idx, val in enumerate(rev_list)
        ]
        string = ''.join(result_list[::-1]).replace('*', '')
        return string

    def from_roman(self, string):
        """
          Convert roman numeral string into number representation
        """
        val = prev = 0
        for char in string[::-1]:
            cur = self.rom_dict[char]
            if prev > cur:
                val -= cur
            else:
                val += cur
            prev = cur
        return val

    def roman_str_gen(self, value=0, power=0, base=10):
        """
          This function calculates the roman numeral representation of a number value passed in and returns the roman numeral representation
        """
        digit_place = base**power
        val = int(value) * digit_place
        upper = lower = 'I'
        roman_string = ''

        # Takes care of cases where the value is 0 or already present
        if self.get_key(val):
            return self.get_key(val)

        # Find the boundary for the value observed
        for k, v in self.rom_dict.items():
            if v >= val:
                lower, upper = upper, k
                break
            lower = upper = k

        # Find starting value to generate numeral string
        if abs(self.rom_dict[upper] - val) <= digit_place:
            roman_string = self.subtract_val(val, upper)
        else:
            roman_string = self.add_val(val, lower)

        return roman_string

    def add_val(self, target=0, start='', base=10, max_repeat=3):
        """
          This function calculates the string representation of numers such as VII=7, XI=11, LCC=60, and DCCC=800, where the roman numeral representation has to add a value, in order to represent the number accurately. 
        """
        is_match = False
        power = repeat = 0
        test_string = f'{start}{self.get_key(base**power)*repeat}'

        while is_match == False:
            if self.from_roman(test_string) == target:
                is_match = True
            elif self.from_roman(
                    test_string) != target and repeat >= max_repeat:
                power += 1
                repeat = 0
            else:
                repeat += 1
                test_string = f'{start}{self.get_key(base**power)*repeat}'
        return test_string

    def subtract_val(self, target=0, start='', base=10):
        """
          This function calculates the string representation of numers such as IV=4, IX=9, XL=40, and XM=90, where the roman numeral representation has to subtract a value, in order to represent the numeral accurately. 
        """
        is_match = False
        power = 0
        while is_match == False:
            test_string = f'{self.get_key(base**power)}{start}'
            if self.from_roman(test_string) == target:
                is_match = True
            power += 1
        return test_string

    def get_key(self, val):
        """
          Returns the key for an associated value within Roman numeral table
        """
        for key, value in self.rom_dict.items():
            if val == value:
                return key
        return False
