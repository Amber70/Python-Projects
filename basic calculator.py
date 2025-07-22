#function to add two number
def add(num1,num2):
    return num1+ num2
#function to subtract two number
def subtract(num1,num2):
    return num1- num2
#function to multiply two number
def multiply(num1,num2):
    return num1* num2
#function to divde two number
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
#function to calculate average of two numbers
def average(num1,num2):
    return (num1+ num2)/2


print("Basic Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
