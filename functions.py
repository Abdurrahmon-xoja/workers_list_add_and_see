import json

def add_workers(name,age,position):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        array_in_data = data["workers"]
        add_variables = {"name": name, "age": age, "position": position}
        array_in_data.append(add_variables)
