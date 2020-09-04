from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    second = input("\nPlease give a last name: ")
    if second == 'q':
        break
    formatted_name = get_formatted_name(first,second)
    print("\nNeatly formatted name: " + formatted_name + ".")