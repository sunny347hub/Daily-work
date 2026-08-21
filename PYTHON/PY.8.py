operator = input ("enter the operation you want to perform (+, -, *, /): " )
num1 = float(input("Enter the number : "))
num2 = float(input("Enter the number : "))
if (operator == "+"):
    result = num1 + num2
    print(f"the result of {num1} + {num2} is : {result}")
elif (operator == "-"):
    result = num1 - num2
    print(f"the result of {num1} - {num2} is : {result}")
elif (operator == "*"):
    result = num1 * num2
    print(f"the result of {num1} * {num2} is : {round(result, 2)}")
elif (operator == "/"):
    if num2 != 0:
        result = num1 / num2
        print(f"the result of {num1} / {num2} is : {round(result, 2)}")
    else:
        print("WITH ZERO DIVISION IS IMPOSSIBLE")
else:
    print("ERROR (INVALID OPERATION).")