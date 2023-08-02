"""
  Lesson 2: ex1.py
"""
import datetime

# 1. Create a format string to display the name and age of a person.

# INSERT YOUR CODE HERE
print("name: {}, age: {}".format("John Doe", 28))
print("name: {0}, age: {1}".format("John Doe", 28))
print("name: {name}, age: {age}".format(age=28, name="John Doe"))
print("name: {0[name]}, age: {0[age]}".format({"name": "John", "age": 28}))

people: list[dict] = [
    {"name": "sato",  "age": 10},
    {"name": "kato",  "age": 13},
    {"name": "naito", "age": 20}
]
print("name: {0[0][name]}, age: {0[0][age]}".format(people))
print("name: {0[1][name]}, age: {0[1][age]}".format(people))
print("name: {0[2][name]}, age: {0[2][age]}".format(people))

print("name: {name}, age: {age}".format(**(people[0])))


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p: Person = Person("ito", 78)
print("name: {0.name}, age: {0.age}".format(p))


# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

# INSERT YOUR CODE HERE
print("{:<10}".format("hello"))
print("{:^10}".format("hello"))
print("{:>10}".format("hello"))
print("{:=<10}".format("hello"))
print("{:=^10}".format("hello"))
print("{:=>10}".format("hello"))

# 3. Show different representations of an integer.

# INSERT YOUR CODE HERE
print("b: {:5b}".format(10))
print("d: {:5d}".format(10))
print("o: {:5o}".format(10))
print("x: {:5x}".format(10))
print("X: {:5X}".format(10))

print("b: {:05b}".format(10))
print("d: {:05d}".format(10))
print("o: {:05o}".format(10))
print("x: {:05x}".format(10))
print("X: {:05X}".format(10))

print("b: {:#09b}".format(10))
print("d: {:#09d}".format(10))
print("o: {:#09o}".format(10))
print("x: {:#09x}".format(10))
print("X: {:#09X}".format(10))

print("b: {0:b} {0:-b} {0:+b} {0: b}".format(0))
print("b: {0:b} {0:-b} {0:+b} {0: b}".format(5))
print("b: {0:b} {0:-b} {0:+b} {0: b}".format(-5))

# 4. Format a floating-point number with fixed precision.

# INSERT YOUR CODE HERE
print("d: {:.4f}".format(123456789.12345678))
print("d: {:,.4f}".format(123456789.12345678))
print("d: {:030.4f}".format(123456789.12345678))
print("d: {:030,.4f}".format(123456789.12345678))
print("d: {:.4%}".format(10.12345678))

print("Today is: {0:%a %b %d %H:%M:%S %Y}".format(datetime.datetime.now()))

age: int = 200
print(f"age: {age:+5d}")
print(f"age: {200:+5d}")
print(f"Today is: {datetime.datetime.now():%a %b %d %H:%M:%S %Y}")
