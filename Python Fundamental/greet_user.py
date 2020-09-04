import json
filename = 'username.json'
with open(filename) as file_obj: # this portion of works are only load the json file and print it(only read not write)
    name = json.load(file_obj)
    print("Welcome back, " + name + "!")
