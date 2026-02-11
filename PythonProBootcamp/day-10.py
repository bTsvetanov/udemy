def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def calculator(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Invalid operation"
while True:
    a = int(input("Enter a number: "))
    print("""Choose the operation you want to perform:
        Addition (+)
        Subtraction (-)
        Multiplication (*)
        Division (/)""")
    operation = input("Pick an operation: ")
    
    b = int(input("Enter another number: "))
    result = calculator(a, b, operation)
    print(f"{a} {operation} {b} = {result}")
    

    more_calculations = input("Do you want to perform another calculation? Type 'yes' or 'no': ")
    if more_calculations == "no":
        break
    else:        print("\n" * 50)

