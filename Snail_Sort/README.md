# Solution

### _Overview:_
The idea is to move in a clock-wise motion, until the center of the 
n  n array is reached.  I decided to use conditionals to implement a solution.

### _Pseudo code:_
1.) Start at the beginning of 2D array  (0,0)<br>

2.) Continue going to the right by `col +=1`
    - Once the end is reach, or the next point is part of the list, pivot and move in the next direction to the next point.<br>

3.) Continue to pivot and move until the length of the returnd list is equal to the amount of entries in the square matrix, or nn array<br>

`len(results) = n*n` is the end point of the function
    
    Movement = mov
    
    Clock-wise:  
    Right (R) ---> Down (D) ---> Left (L) ---> Up (U) repeat
    
    R:                     D:
        mov % 4 == 0          mov %4 == 1
        col+=1                row+=1
    L:                     U:
        mov %4 == 1           mov % 4 == 3
        col-=1                row-=1                