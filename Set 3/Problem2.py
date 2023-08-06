# Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
"""
Input: Add "John": 25, Update "John": 26, Delete "John"
Output: "{}, {'John': 26}, {}"
"""

dict = {}

print(dict)

dict.update( {"John" : 25} )
print(dict)

dict.update( {"John" : 26} )
print(dict)

del dict["John"]
print(dict)
