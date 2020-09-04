#print(5/0)
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter q to quit.")

try:
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        answer = int(first_number) / int(second_number)
        print(answer)
except ZeroDivisionError:
    print("You can't divide by zero.")

# zero Division error try catch block
print("Give me two numbers, and I'll divide them.")
print("Enter q to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer) # any code that depends on the try block executing successfully goes in the else block
'''

# file not found exception error

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()  # read this file and store it into contents
    except FileNotFoundError:
        pass # here the exception failing silently rather than show a message,don't need to report every exception you catch and continue on as if nothing happened
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
    else:  # else block is execute if the try block was executed successfully
        words = contents.split()
        num_words = len(words)
        print(words)
        print("The file " + filename + " has about " + str(num_words) + " words.\n")


filenames = ['alice.txt','digits.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for i in filenames:
    count_words(i)



