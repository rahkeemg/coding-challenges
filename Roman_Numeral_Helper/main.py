from RomanNumerals_static import RomanNumerals
from RomanNumerals import RomanNumerals as rn

test = 'MMMDCCXXIV'
test2 = 'MCD'
test3 = 'MCID'

# num = RomanNumerals.from_roman(test2)
# print(num)

# test_num = 1000
# roman = RomanNumerals.to_roman(test_num)
# print(test_num, roman)

test_num_2 = 3879
converter = rn()
roman = converter.to_roman(test_num_2)
print(roman)