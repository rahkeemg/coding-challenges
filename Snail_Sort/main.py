from Snail import Snail

my_snail = Snail()

array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]

for i in range(0, len(array1)):
    print(array1[i])

my_snail.set_map(array1)
print(my_snail.travel_map(), '\n\n')


array2 = [[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 7], [7, 8, 9, 7]]
expected2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(array2)):
    print(array2[i])

my_snail.set_map(array2)
print(my_snail.travel_map(), '\n\n')

array3 = [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8],
          [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10],
          [16, 15, 14, 13, 12, 11]]
expected3 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
]

for i in range(0, len(array3)):
    print(array3[i])

my_snail.set_map(array3)
print(my_snail.travel_map(), '\n\n')