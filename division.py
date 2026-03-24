def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Division =", divide(num1, num2))
