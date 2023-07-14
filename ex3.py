"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

# INSERT YOUR CODE HERE
print("Pizza" * 42)

# 2. Insert space between each output and print it out again.

# INSERT YOUR CODE HERE
print("Pizza " * 42)

# 3. Save your favourite food into a variable and print it out 42 times

# INSERT YOUR CODE HERE
favorite_food = "Pizza"
print(favorite_food * 42)

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

# INSERT YOUR CODE HERE
your_favorite_food: str = "sushi"
favorite_food, your_favorite_food = your_favorite_food, favorite_food
print(favorite_food)
print(your_favorite_food)
