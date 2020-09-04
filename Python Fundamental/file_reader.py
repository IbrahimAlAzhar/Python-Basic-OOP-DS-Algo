'''
with open('digits.txt') as file_object:
    contents = file_object.read()
     # print(contents) # this print use extra blank line after the output
    print(contents.rstrip())  # rstrip function remove extra whitespace characters from the right side of the string

# if the text file is properly other directory from the python file then you have to use absolute path rather than relative path(relative path which use in previous code)
file_path = 'C:/Users/ehmatthes/other_files/text_files/filename.txt' # here using absolute paths,so you can read files from any location on your systems
with open(file_path) as file_object:


filename = 'digits.txt'
with open(filename) as file_object:
    for i in file_object: # print the file_object line by line
        # print(i) # there are invisible newline character is at the end of each line in the text file,print create its own newline
        print(i.rstrip()) # rstrip remove the extra blank line

# making a list of lines from a file
filename = 'digits.txt'
# writing to the text file
with open(filename,'w') as file_object:  # 'w' means tells python that we want to open the file in write mode,read mode('r'),append mode('a'),read and write file('r+')
    file_object.write("I love programming.\n")
    file_object.write("My favourite programming language is python.\n")
    file_object.write("3.141592653589793238462643383279 ")

with open(filename) as file_object:
    lines = file_object.readlines() # readlines method() takes each line from the file and stores it in a list,this list is then stored in lines,store the file_object inside the 'lines' list
pi_string = ''
for i in lines:
    # pi_string += i.rstrip() # rstrip is using for remove the space on right side,but it didn't remove the space in left side
    pi_string += i.strip()  # strip remove the space in left and right side
print(pi_string[:28])  # print first 15 digits
print(len(pi_string))
birthday = input("Enter your birthday,in the form of ddmm: ")
if birthday in pi_string:
    print("Your birthday appears in the first 30 digits of pi!")
else:
    print("Your birthday does not appear in the first 30 digits of pi!")
'''
filename = 'digits.txt'
with open(filename,'w') as file_object: # 'w' is using for writing
    file_object.write("django framework is my favourite framework in python language\n")
    file_object.write("The python language is best language in the glove.\n")

with open(filename,'a') as file_object:  # 'a' is using for append
    file_object.write("Python is very useful in Data Science.\n")



