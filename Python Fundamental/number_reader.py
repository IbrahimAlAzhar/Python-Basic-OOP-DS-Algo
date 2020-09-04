import json
filename = 'numbers.json' # this json file declare in 'number_writter.py' file
with open(filename) as file_obj: # here we open in read mode,because we want just display the number
    num = json.load(file_obj) # we load the json file where we declare in 'number_writer.py' file

print(num)
