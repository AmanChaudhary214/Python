# Initialize dictionary with default values
"""
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

output = {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

"""

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

output = {}

for i in employees :
  output.update( {i : defaults} )

print(output)  
