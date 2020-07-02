
# Instructions


## Roman Numeral Helper

### Task

Create a RomanNumerals class that can convert a roman numeral **to and from an integer value**. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: `1000=M`, `900=CM`, `90=XC`; resulting in `MCMXC`. 2008 is written as `2000=MM`, `8=VIII`; or `MMVIII`. 1666 uses each Roman symbol in descending order: `MDCLXVI`.

### Examples

```
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
```

### Help
| Symbol | Value |
| :---:  | :----:|
| I | 1 | 
| V | 5 | 
| X | 10 | 
| L | 50 | 
| C | 100 | 
| D | 500 | 
| M | 1000 |


--------------
## Roman Numeral Encoder

Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: `1000=M`, `900=CM`, `90=XC`; resulting in `MCMXC`. 2008 is written as `2000=MM`, `8=VIII`; or `MMVIII`. 1666 uses each Roman symbol in descending order: `MDCLXVI`.

### Example:

`solution(1000) # should return 'M'`

### Help:

| Symbol | Value |
| :---:  | :----:|
| I | 1 | 
| V | 5 | 
| X | 10 | 
| L | 50 | 
| C | 100 | 
| D | 500 | 
| M | 1000 |
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals


------------

## References

[Roman Numeral Helper](https://www.codewars.com/kata/51b66044bce5799a7f000003)<br>
[*Roman Numeral Encoder](https://www.codewars.com/kata/51b62bf6a9c58071c600001b)<br>

\*\[This link is a different challenge however, its functionality is included within this project.\]