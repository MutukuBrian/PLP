def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero!"
        result = num1 / num2
    else:
        return "Invalid operation choice!"

    return f"{num1} {operation} {num2} = {result}"

print(calculator())