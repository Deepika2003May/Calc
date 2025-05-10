# Simple Calculator (Only Multiply and Divide)
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Simple Calculator")
print("1. Multiply\n2. Divide")

choice = input("Enter choice (1/2): ")

if choice in ('1', '2'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", multiply(num1, num2))
    elif choice == '2':
        print("Result:", divide(num1, num2))
else:
    print("Invalid input")
