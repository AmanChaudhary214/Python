# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

output = {'name': 'Kelly', 'salary': 8000}

"""

sample_dict = {
                "name": "Kelly",
                "age": 25,
                "salary": 8000,
                "city": "New york"
              }

keys = ["name", "salary"]

output = {}

for i in keys :
  for j in sample_dict :
    if i==j :
      output.update( {i : sample_dict[j]} )

print(output)