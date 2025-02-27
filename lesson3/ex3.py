"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

# INSERT CODE HERE
print(shopping_list)
print(sorted(shopping_list))
print()

# 2. Sort the list using .sort() method and print that list

# INSERT CODE HERE
print(shopping_list)
shopping_list.sort()
print(shopping_list)
print()

# 3. Use the built-in function reversed(), reverse the list and print that list

# INSERT CODE HERE
print(shopping_list)
print(list(reversed(shopping_list)))
print()

# 4. Reverse the list using sort() method and print the list

# INSERT CODE HERE
print(shopping_list)
shopping_list.sort(reverse=True)
print(shopping_list)
print()

# 5. Reverse the list using sorted() method and print the list

# INSERT CODE HERE
print(shopping_list)
print(sorted(shopping_list, reverse=True))
