"""
  Lesson 5: ex1.py
"""

# 1. Create even() function that return "I am even!" if number is even
#    or "I am odd!" if the number is odd.

# INSERT YOUR CODE HERE


def even(value: int) -> str:
    return "I am even!" if value % 2 == 0 else "I am odd!"


print(even(1))
print(even(2))
print(even(3))
print(even(4))


# 2. Create safe_even() function, that will output "I am not number!" if
#    the input is not an number otherwise will work same as even()

# INSERT YOUR CODE HERE

def safe_even(value: int) -> str:
    if not isinstance(value, int):
        return "I'm not number"
    return "I am even!" if value % 2 == 0 else "I am odd!"


print(safe_even(1))
print(safe_even("aaa"))

# 3. Create a function fizz_buzz(),
#    replacing any number divisible by three with the word "fizz",
#    and any number divisible by five with the word "buzz",
#    and any number divisible by both 3 and 5 with the word "fizzbuzz",
#    and number if number is not divisible by any.

# INSERT YOUR CODE HERE


def fizz_buzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    return str(n)

# 4. Execute fizz_buzz() function from 1 to the 100

# INSERT YOUR CODE HERE


print(list(map(fizz_buzz, range(1, 101))))
