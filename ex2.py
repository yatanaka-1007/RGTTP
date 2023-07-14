"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.

# INSERT YOUR CODE HERE
PRICES: dict = {
    'Apples':  2.99,
    'Milk':    1.79,
    'Bread':   3.49,
    'Chicken': 6.99,
    'Pasta':   2.49,
}


def calc_total_cost(items: list) -> float:
    return sum([PRICES[item] for item in shopping_list])


shopping_list: list = ['Apples', 'Milk', 'Bread', 'Chicken', 'Pasta']
print(shopping_list)

# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.

# INSERT YOUR CODE HERE
print("total cost: " + str(calc_total_cost(shopping_list)))

# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?

# INSERT YOUR CODE HERE
shopping_list = shopping_list + ["Milk"] * 4
print("total cost: " + str(calc_total_cost(shopping_list)))

# 4. Print out every item of your shopping list on a new line.
# INSERT YOUR CODE HERE
for item in shopping_list:
    print(item)
