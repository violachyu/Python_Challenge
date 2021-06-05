'''Python Challenge - 6
Create a function called fizzbuzz. It will take 1 parameter, a number. For example: 150
This is a version of the popular FizzBuzz challenge. You will need to return 'Fizz' if a number is divisible by 3, 'Buzz' if a number is divisible by 5, 'FizzBuzz' if the number is divisible by both 3 and 5, and return the number if none of the above applies.
For example: fizzbuzz(150) should return 'FizzBuzz' because it is divisible by 5 and 3.
'''

# enter your code below
def fizzbuzz(number):
    result = ''
    if (number % 3 == 0 or number % 5 == 0):
        if number % 3 == 0:
            result += 'Fizz'
        if number % 5 == 0:
            result += 'Buzz'
    else:
        result = number
    return result