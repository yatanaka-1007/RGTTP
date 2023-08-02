"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

# INSERT YOUR CODE HERE
person: list = ["John", 80, "Engineer"]
print("name: {0[0]}\nage: {0[1]}\noccupation: {0[2]}".format(person))

# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

# INSERT YOUR CODE HERE
book: dict = {
    "title": "Understanding Linux Network Internals",
    "author": "Christian Benvenuti",
    "publication_year": 2006,
}
print("The guidebook {0[title]} by {0[author]} was published in "
      "{0[publication_year]}.".format(book))

# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

# INSERT YOUR CODE HERE
spaceship: dict = {
    "name": "Apollo 13",
    "type": "Human spaceflight",
    "purpose": "Crewed lunar landing attempt",
}
print("The spaceship is called the {name}. It is a {type} used "
      "for {purpose}.".format(**spaceship))
