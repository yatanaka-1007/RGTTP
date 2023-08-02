"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

# INSERT YOUR CODE HERE
versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}
for key, value in versions.items():
    print("The version number of {} is {}".format(key, value))

print()

# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE
for key, value in versions.items():
    print("The version number of {} is {{{}}}".format(key, value))

print()

# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE
for key, value in versions.items():
    print("The version number of {} in decimal is {:#d}".format(key, value))
    print("The version number of {} in binary is {:#b}".format(key, value))
    print("The version number of {} in hexadecimal is {:#X}".format(key,
                                                                    value))
