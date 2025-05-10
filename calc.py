# Simple Calculator (Only Division)
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Simple Calculator - Division Only")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = divide(num1, num2)
print("Result:", result)
