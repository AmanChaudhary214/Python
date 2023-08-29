import json

file_path = "snacks.json"
initial_data = [
   
]
try:
    with open(file_path, "r") as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    existing_data = []

all_snacks_data = initial_data + existing_data


with open(file_path, "w") as json_file:
    json.dump(all_snacks_data, json_file, indent=4)


new_data = [
    {"name": "Pretzels", "price": 1.0, "availability": False},
    {"name": "Popcorn", "price": 2.0, "availability": True}
]

try:
    with open(file_path, "r") as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    existing_data = []


all_snacks_data = existing_data + new_data


with open(file_path, "w") as json_file:
    json.dump(all_snacks_data, json_file, indent=4)
