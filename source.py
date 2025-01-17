def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print("Result:", result)

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    result = calculate(num1, num2, operator)
    print("Result:", result)
    
    repeat = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if repeat != 'yes':
        break