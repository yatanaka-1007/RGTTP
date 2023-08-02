"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False

# INSERT CODE HERE


class ShoppingList(object):
    def __init__(self,
                 shopping_list: list[str] = ['apples', 'milk', 'bread',
                                             'carrot', 'pasta']):
        self.shopping_list = shopping_list

    def in_list(self, item: str) -> str:
        if item in self.shopping_list:
            return f"'{item}' is in the shopping list."
        else:
            return f"'{item}' is not in the shopping list."

    def __str__(self) -> str:
        return f"My shopping list: {self.shopping_list}"

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.shopping_list == other.shopping_list


monday: ShoppingList = ShoppingList()
print("##### Monday #####")
print(monday)
print(monday.in_list("milk"))
print(monday.in_list("banana"))

print("##### Tuesday #####")
tuesday: ShoppingList = ShoppingList(["banana", "apple"])
print(tuesday)
print(tuesday.in_list("milk"))
print(tuesday.in_list("banana"))
print("Monday and Tuesday is the same : {}".format(monday == tuesday))
print("Monday and Tuesday is the same : {}".format(tuesday == monday))

print("##### Wednesday #####")
wednesday: ShoppingList = ShoppingList(['apples', 'milk', 'bread',
                                        'carrot', 'pasta'])
print(wednesday)
print(wednesday.in_list("milk"))
print(wednesday.in_list("banana"))
print("Monday and Wednesday is the same : {}".format(monday == wednesday))
print("Monday and Wednesday is the same : {}".format(wednesday == monday))
