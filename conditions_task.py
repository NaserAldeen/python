first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

if first_number.isdigit() and second_number.isdigit():
    operation = input("Choose the operation (+, -, /, *): ")
    if len(operation) == 1 and operation in "+-/*":
        #The eval() function evaluates a mathematical expression in a string
        print(eval(first_number+operation+second_number))
    else:
        print("You've entered invalid operation")
else:
    print("You've entered invalid inputs")
