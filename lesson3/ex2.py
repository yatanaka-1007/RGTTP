"""
  Lesson 3: ex2.py
"""

# 1. Create a list of number 0 to 9 using a for loop.
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# INSERT CODE HERE
numbers: list[int] = []
for i in range(10):
    numbers.append(i)
print(numbers)

numbers = list(range(10))
print(numbers)

# 2. Create a list of number from 0 to 9 the power of 2 using a for loop.
#
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# INSERT CODE HERE
powered_numbers: list[int] = []
for i in range(10):
    powered_numbers.append(i ** 2)
print(powered_numbers)

powered_numbers = [i ** 2 for i in range(10)]
print(powered_numbers)

# 3. Create a list of lists, which contains elements that are
# number, number(to the power of 2), number(to the power of 3)
#
# [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64],
#  [5, 25, 125], [6, 36, 216], [7, 49, 343], [8, 64, 512],
#  [9, 81, 729]]

# INSERT CODE HERE
lists: list[list[int]] = []
for i in range(10):
    lists.append([i, i ** 2, i ** 3])
print(lists)

lists = [[i, i ** 2, i ** 3] for i in range(10)]
print(lists)

# 4. Add condition in a for loop, that only numbers that are odd are added.
#
# [[1, 1, 1], [3, 9, 27], [5, 25, 125], [7, 49, 343], [9, 81, 729]]

# INSERT CODE HERE
odd_lists: list[list[int]] = []
for i in range(10):
    if i % 2 == 1:
        odd_lists.append([i, i ** 2, i ** 3])
print(odd_lists)

odd_lists = [[i, i ** 2, i ** 3] for i in range(10) if i % 2 == 1]
print(odd_lists)

# 5. Create a nested lists in a list with a for loop:
# [['ax', 'bx', 'cx', 'dx', 'ex'],
#  ['ay', 'by', 'cy', 'dy', 'ey'],
#  ['az', 'bz', 'cz', 'dz', 'ez']]

# INSERT CODE HERE
str_lists: list[list[str]] = []
for chr2 in "xyz":
    str_list: list[str] = []
    for chr1 in "abcde":
        str_list.append(chr1 + chr2)
    str_lists.append(str_list)
print(str_lists)

str_lists = [[chr1 + chr2 for chr1 in "abcde"] for chr2 in "xyz"]
print(str_lists)
