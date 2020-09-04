import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json' # here declare the filename in json format and store the numbers in this file
# this code only for writing,we can't show output in this file
with open(filename,'w') as file_obj: # open the file in write mode
    json.dump(numbers,file_obj)  # json.dump is use for to store the list numbers in json file 'file_obj(numbers.json)'

