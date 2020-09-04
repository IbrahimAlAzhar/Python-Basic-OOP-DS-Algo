import json
# load the username,if it has been stored previously,otherwise prompt for the username and store it
'''
def greet_user():
    """greet the user by name"""
    username = input("What is your name? ")
    filename = 'username.json'
    try:  # if the file is already write in 'username.json' file
        with open(filename) as file_obj:  # if the name is already taken,then just load it into name variable(only read)
            name = json.load(file_obj)
    except FileNotFoundError:  # if the name is not taken already then take it(applying write activities)
        name = input("What is your name?")
        with open(filename, 'w') as file_obj:
            json.dump(username, file_obj)  # store the value of username in file_obj
            print("We'll remember you when you come back," + username + "!")
    else:  # if the try block works then goes to else block
        print("Welcome back, " + username + "!")

greet_user()
'''
def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as file_obj: # if already has a username then just read it and return it
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username # if the username already set it in json file then store to 'username' variable and return it


def get_new_username(): # if the username are not created then prompt for a new username
    """prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename,'w') as file_obj: # here the 'username.json' file are empty,so we write in this file
        json.dump(username,file_obj) # store the username value into file_obj json file,but here we are not use json file,we just pass the username variable
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()  # call the 'get_stored_username()' function and if the username is already store in json file then store into username variable and return into it
    if username:
        print("Welcome back, " + username + "!")
    else:  # if the username does not exist
        username = get_new_username()  # store the username from get_new_username() function,and in this function we also store the 'username' in json file
        print("We'll remember you when you come back, " + username + "!") # here we are not use the json file 'file_obj',if we need to use this username in another file then we just call this json file
greet_user()