## Implementation overview

The main part of this program can be broken down into two main parts. These main parts have smaller methods that help fulfill the overall goal of the function. 

In this markdown file, we will approach the funtions as an overview.  Not every funnction will be described in detail.  

The Python files are available for any to look at the code files. 

### `to_roman()`
This function takes a base_10 number and creates the roman numeral equivalent through 5 main steps.  

##### _Step 1:_
```
int(3879)  ->  "3879"
```

##### _Step 2:_
Reverse the string representation of the input integer.  This way, the problem can be broken down into smaller parts

```
# Number as a string representation
"3879"

# Reversed string representation
"9783"
```

##### _Step 3:_

Turn the reversed string into a list and turn the single digit entries back into integers.  
I am doing it this way so that the indicies will be the actual representation of the digit placement.

Once this is done, I use the indicies as the exponent to find which roman numeral is closest to the value in question.  Refer to the example below for more information.

```
# Reversed string to list-of-strings/chars representation
"9783"   ->  ['9','8','7','3']

indicies:    0   1   2   3
             |   |   |   |
elements:  ['9','8','7','3']

# The indicies will the power by wich we raise 10.
# Examples: 

# 9 is in the 'ones' place
int('9') * 10**0 = 9 * 1 = 9

# 8 is in the 'tens' place
int('8') * 10**1 = 8 * 10 = 80

# 7 is in the 'hundreths' place
int('7') * 10**2 = 7 * 100 = 700

# 3 is in the 'thousandths' place
int('3') * 10**3 = 3 * 1000 = 3000

# Now, when we look at the values as such and add them up, we get our inital input value of 3789
3000 + 700 + 80 + 9 = 3789
```

The original value is `3879.`  With the string reversed and stored in a list `['9','8','7','3']`, we can now generate its roman numeral representation

##### _Step 4:_

Find the boundary for the number in question and typecast the values as integers. Once we have the lower and upper boundary, we can begin to construct the Roman Numeral string, depending on proximity of the value to the respective boundary. 


```
Example 1 -- The One's Digit place: 


indicies:    0   1   2   3
             |   |   |   |
elements:  ['9','8','7','3']

# 9 is in the 'ones' place
int('9') * 10**0 = 9 * 1 = 9

# The value falls within one step of the upper boundary.
# The string will start at the roman representation of 10 and step 
# down by 1. 
#
# Since we are dealing with the one's digit place, 
# our step size will be 1 = 10**0

value = 9

'V' <  value  < 'X'
 5  <    9    <  10

## Pseudo code for constructing Roman Numeral string

# Compare the difference of the upper and lower value to deterine which
# one should be used.  
#
# In the example below, our value is 9 and our step
# sizes is 1=10**0 because we are dealing with the one's place

|value - 5 | = 4  # lower boundary steps to value
|value - 10| = 1  # uppoer boundary steps to value

# Since the step size is within one of the upper boundary, we will start with
# the upper boundary, 'X', and append 'I' to the beginning, to get 
# the equivalent value as a roman numeral  

start at 'X'
append 'I' to the beginning of the string
if 'IX' == 9:
  return 'IX'

# This is the process that is repeated for each value until the full
# string has been generated.  

NOTE: The step size will change as you are looking at different digit 
place.  If the value being observed already has a Roman numeral representation within the table of roman numeral values, we will return the value immediately and move onto the next digit place.



Example 2 -- The Ten's Digit place:



indicies:    0   1   2   3
             |   |   |   |
elements:  ['9','8','7','3']

# 8 is in the 'tens' place
int('8') * 10**1 = 8 * 10 = 80

# The value falls within three step of the lower boundary
# the string will start at the roman representation of 50 and step 
# up by ten, until we reach 80, or until the amount of repeated characters
# exceeds 3. 
#
# The step size will be 10 = 10**1 since we are dealing with the ten's digit place

value = 80

'L' <  value  < 'C'
50  <   80    <  100

# Since the step size is within 3 of the lower boundary, we will start with
# the lower boundary, 'L', and append 'X' to the end, to get 
# the equivalent value as a roman numeral  
# 
# NOTE: The only numerals that can follow another and have 
# up to 3 consecutive repeats are powers of 10:
#
#     I = 1   = 10**0
#     X = 10  = 10**1 
#     C = 100 = 10**2  
#
# The possibility of inapporpriate numeral strings arises, but they will not match
# the value and will be immediately replaced as soon as the repetitions 
# exceed 3. Once the max repetition limit exceeds 3, the next power up is selected.

start at 'L'
add up to 3 'I's to the end of the starting string 
  and check each time to see if the roman numeral equals the value
if it does nto work, then go to the next power of 10 and repeat the process.

The reutrned numeral string will be 'LIII' for the value of 50

# This is the process that is repeated for each value until the full
# string has been generated.
```

This process is repeated until all digit places within the number have been visited and store in a list, where the indicies will repesent the digit place.

**Note:** 0 is a value that needs to be addressed.  We are returning asterisks,  '\*', to take care of this value. The value is stripped out and replaced with an empty character, '', when the result is returned. 

##### _Step 5:_

Take the results from step 5 and store each as an entry within a list.
Once all digit places have been addressed, the list will be reversed, back to the original order, special characters will be stripped, and a string representation of the initial value will be returned.

This is the last and final step.  Below is a recap of each step upt to step 5.
```
# After step 4, we will have a list with the values:

Overview / Recap

~~~~~~~
Step_1
~~~~~~~
# Initial value coverted to string
3879  -> '3879'

~~~~~~~
Step_2
~~~~~~~
# String reversed and converted to list
"3879" -> ['3','8','7','9']

~~~~~~~
Step_3
~~~~~~~
# reverse the list from step 3 
['3','8','7','9'] -> ['9','8','7','3']

~~~~~~~
Step_4
~~~~~~~
# convert values in list to roman numeral representation
['9','8','7','3'] -> ['IX', 'LXX', 'DCCC', 'MMM']

~~~~~~
Step_5
~~~~~~
# Now with the reversed list, we will revrse the results list
# and concatenate the entries into a string

results_list                    reversed_result_list
['IX', 'LXX', 'DCCC', 'MMM'] -> ['MMM', 'DCCC', 'LXX', 'IX' ]

reversed_result_list              final_string
['MMM', 'DCCC', 'LXX', 'IX' ] ->  'MMMDCCCLXXIX'

# The final_string is the returned roman numeral representation
return 'MMMDCCCLXXIX'
```

### `from_roman()`

With this implementation, I decided to go from the tail of the string to the head. This way, I can immediately capture numerals such as 9, where its proper form is written as IX, instead using repeated values as seen in VIIII.  

**Note**: This can be done from the head to the tail.  You will have to ensure that you capture the right format in doing so. For me, it was easier doing a look-behind implementation to take care of subtraction scenarios, such as IX = 9.