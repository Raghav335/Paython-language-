#code for calculator program

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "🤦BINGO, Division is not possible because denominator is 0 here🤦"
    return x / y

print("Calculator shortcuts")
print("1. ➕️")
print("2. ➖️")
print("3. ️✖️")
print("4. ➗️")

choice = input("Enter your choice: ")

if choice in ["1", "2", "3", "4"]:
    num1 = int(input("Enter first number: "))
    num2 =int(input("Enter second number: "))

    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", divide(num1, num2))
else: print("Invalid operator choosen ")