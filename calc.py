# Simple Calculator (Only Division)
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Simple Calculator - Division Only")

First1 = float(input("Enter first number: "))
Second2 = float(input("Enter second number: "))

result = divide(First1, Second2)
print("Result:", result)
