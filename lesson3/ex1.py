"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']
print(shopping_list)

# 1. Add banana to a shopping list.

# INSERT CODE HERE
shopping_list.append("banana")
print(shopping_list)

# 2. Add chocolate in the third position in your shopping list

# INSERT CODE HERE
shopping_list.insert(2, "banana")
print(shopping_list)

# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

# INSERT CODE HERE
shopping_list.extend(['chocolate', 'carrot', 'avocado'])
print(shopping_list)

# 4. Remove first chocolate only

# INSERT CODE HERE
try:
    shopping_list.remove('chocolate')
except ValueError as e:
    print(e)
print(shopping_list)

# 5. Remove last item from the list

# INSERT CODE HERE
try:
    shopping_list.pop()
except IndexError as e:
    print(e)
print(shopping_list)

# 6. Remove third item from the list

# INSERT CODE HERE
try:
    shopping_list.pop(2)
except IndexError as e:
    print(e)
print(shopping_list)

# 7. Count how many carrots are in the shopping list?

# INSERT CODE HERE
print(shopping_list.count('carrot'))

# 8. Get the index of the chocolate (careful can throw traceback)

# INSERT CODE HERE
try:
    print(shopping_list.index('chocolate'))
except ValueError as e:
    print(e)

# 9. Get the index of carrot, make sure this code is executed

# INSERT CODE HERE
try:
    print(shopping_list.index('carrot'))
except ValueError as e:
    print(e)
