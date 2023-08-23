"""
  Lesson 5: ex2.py
"""

# 1. Write a while true loop to print "Forever" forever

# INSERT YOUR CODE HERE
loop_num: int = 100
while True:
    print("Forever")
    loop_num -= 1
    if loop_num <= 0:
        break

# 2. Write a while loop to print numbers from 0 to 42

# INSERT YOUR CODE HERE
num: int = 0
while num <= 42:
    print(num)
    num += 1

# 3. Write a while true loop to print numbers from 0 to 42

# INSERT YOUR CODE HERE
num = 0
while True:
    print(num)
    num += 1
    if num > 42:
        break

# 4. Write a while true loop to print numbers from 0 to 45, and instead
#    of 42, print "I am 42!" break at number 45.

# INSERT YOUR CODE HERE
num = 0
while True:
    print(num if num != 42 else "I am 42!")
    num += 1
    if num > 45:
        break

# 5. Write a while-else loop to count to 2, and after that print
#    "It's my turn now!" using else statement.

# INSERT YOUR CODE HERE
num = 0
while num <= 2:
    print(num)
    num += 1
else:
    print("It's my turn now!")
