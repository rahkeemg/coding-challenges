# Implementation

My function to solve this problem assumes that the hexadecimal string is in the following format:

### Input Format:
- starts with a hashtag #
- six hexadecimal characters follow the hashtag

Example: `hex_string = #000000`


## Pseudo code:


* Strip the hashtag from the string and divide the string up into 3 parts, each with two characters of the hexadecimal range `[0,F]`

    `'#000000' ==> ['00','00','00']`

* Convert each grouping into respective decimal base representation

    ` # Hex values [00, 00, 00]`<br>
    ` # Int values [  0, 0,  0] `

* Return the assoociated integer values with respective color as a dictionary

    `{'r': 0, 'g': 0, 'b': 0}`

Refer to [conversion.py](./conversion.py) for code