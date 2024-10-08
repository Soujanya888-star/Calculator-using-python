# Simple calculator program

# Define basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Display options to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Get input for the two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the chosen operation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid Input")
