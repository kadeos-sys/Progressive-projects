#Making a calculator able to do basic operations

def add (x, y):
    return x + y
def subtract (x, y):
    return x - y 
def multiply (x, y):
    return x * y
def divide (x, y):
    if y == '0':
        return 'Error, cannot divide by zero'
    return x / y


# table shows availible operations for user

print("1- add -- 2- subtract -- 3- multiply -- 4- divide")

user_ans = input("enter the operation you want to do, 1, 2, 3, 4: ")

# checks if the input is in the range of operations 
if user_ans in ['1', '2', '3', '4']:
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
   #utilizes the operation and completes the calculation 
    if user_ans == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif user_ans == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif user_ans == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif user_ans == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("invalid input")
    