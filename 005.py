'''Python Challenge - 5
Create a function called mathy. It will take 3 parameters, a string and two numbers.
For example: 'divide', 15, 5
Your function will need to complete the math operation and return the result.
For example: mathy('divide', 15, 5) should return 3.
Options are: add, subtract, multiply, or divide.
'''

def mathy(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'substract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        return num1 // num2

print(mathy('divide', 15, 5))