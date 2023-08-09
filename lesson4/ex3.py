"""
  Lesson 4: ex3.py
"""
from collections import defaultdict
from typing import Any

# 1. Create dictionary using comprehension
# {key, value = i, i**2}

# INSERT YOUR CODE HERE
my_dict1: dict[int, int] = {i: i**2 for i in range(10)}
print(my_dict1)

# 2. Create another comprehension and add +1 to each key's value.
# {key, value = i, i+1}

# INSERT YOUR CODE HERE
my_dict2: dict[int, int] = {i: i+1 for i in range(10)}
print(my_dict2)

# 3. Create 'fruits' defaultdict():
# apple: 10
# orange: 2
# banana: 3
# and for any other key set it's default value to 0

# INSERT YOUR CODE HERE
fruits: defaultdict[Any, Any] = \
    defaultdict(lambda: 0, {
        "apple": 10,
        "orange": 2,
        "banana": 3
    })
for k, v in fruits.items():
    print(f"{k}: {v}")

# 4. Sort the 'fruits' dictionary using sorted() method
# by keys and values, dictionary does not have .sort()

# INSERT YOUR CODE HERE
print(sorted(fruits))
print(dict(sorted(fruits.items(), key=lambda item: item[0])))
print(dict(sorted(fruits.items(), key=lambda item: item[1])))

# 5. Return 'sorted_fruits' dictionary using sorted() method,
# sort by values.

# INSERT YOUR CODE HERE
sorted_fruites: dict[str, int] = dict(sorted(fruits.items(),
                                             key=lambda item: item[1]))
print(sorted_fruites)

# 6. Reverse the 'sorted_fruits' dictionary and print the dictionary.

# INSERT YOUR CODE HERE
reversed_fruites: dict[str, int] = dict(sorted(fruits.items(),
                                               key=lambda item: item[1],
                                               reverse=True))
print(reversed_fruites)
