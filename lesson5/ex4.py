"""
  Lesson 5: ex4.py
"""
from typing import Union

# 1. Write a function get_index() that returns the index of
#    a character in a string

# INSERT YOUR CODE HERE


def get_index(string: str, searching_char: str) -> int:
    for index, char in enumerate(string):
        if char == searching_char:
            return index
    raise ValueError(f"'{searching_char}' is not found in '{string}'")


print(get_index("abcdefg", "d"))

# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.

# INSERT YOUR CODE HERE


def shout(string: str) -> list[str]:
    return list(map(lambda s: s.upper() + "!", string.split(" ")))


print(shout("Hi, it's nice to meet you"))


# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False

# INSERT YOUR CODE HERE


def extract_longer(n: int, string: str) -> Union[list[str], None]:
    result: list[str] = list(filter(lambda s: len(s) >= n, string.split(" ")))
    return result if len(result) != 0 else None


print(extract_longer(2, "Hi, it's nice to meet you"))
print(extract_longer(3, "Hi, it's nice to meet you"))
print(extract_longer(4, "Hi, it's nice to meet you"))
print(extract_longer(5, "Hi, it's nice to meet you"))
