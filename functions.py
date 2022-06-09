import json

def add_workers(name,age,position):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        array_in_data = data["workers"]
        add_variables = {"name": name, "age": age, "position": position}
        array_in_data.append(add_variables)

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=6)

def see():
    with open('data.json', 'r') as file:
        data = json.load(file)
        array_in_data = data["workers"]
        for w in array_in_data:
            print(array_in_data["name"], array_in_data["age"], array_in_data["position"])



