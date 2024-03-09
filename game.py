list_1 = []
list_2 = []

try:
    while True:
        num1 = input("Enter a number to add to the list or press any non-numeric key to go to the second list: ")
        try:
            num1 = int(num1)  # Convert input to integer
            list_1.append(num1)
            print("List 1:", list_1)
        except ValueError:
            print("Moving to the second list...")
            break  # Break out of the loop if non-numeric input is provided

finally:
    print("Final List 1:", list_1)
