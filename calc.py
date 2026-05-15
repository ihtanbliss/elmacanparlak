while True:
    print("Hi! Welcome to the calculator, Please choose the first number.")
    num1 = float(input())
    print("Please choose the second number")
    num2 = float(input())



    print("Please choose an operation(+, -, *, /)")
    operation = input()
    if operation == "+":
        print(int(num1 + num2))
    elif operation == "-":
        print(int(num1 - num2))
    elif operation == "*":
        print(int(num1 * num2))
    elif operation == "/":
        print(int(num1 / num2))