"""
  Lesson 4: ex2.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2
# banana: 3

# INSERT YOUR CODE HERE

fruits: dict[str, int] = {
    "apple": 10,
    "orange": 2,
    "banana": 3
}

# 2. Iterate over fruits in fruits dictionary using for loop,
#    print using f-strings:
#    apple: 10
#    orange: 2
#    banana: 3

# INSERT YOUR CODE HERE
for key, value in fruits.items():
    print(f'{key}: {value}')

# 2. Iterate over the keys in 'fruits' dictionary

# INSERT YOUR CODE HERE
for key in fruits.keys():
    print(f'{key}')

# 3. Iterate over the values in dictionary

# INSERT YOUR CODE HERE
for value in fruits.values():
    print(f'{value}')

# 4. Access value banana using .get() method

# INSERT YOUR CODE HERE
print(fruits.get("banana"))

# 5. Access value mandarin using .get() method,
#    if 'mandarin' doesn't exist, return 0

# INSERT YOUR CODE HERE
print(fruits.get("mandarin", 0))

# 6. Remove all items from the dictionary

# INSERT YOUR CODE HERE
fruits.clear()
print(fruits)
