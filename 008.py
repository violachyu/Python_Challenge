'''Python Challenge - 8
Create a function called check_name.
It will receive 2 parameters, both strings. For example: 'treehouse', 'tree'
Turn both strings into sets.
Return if the second string ('tree') is a subset of the first ('treehouse').
For example, check_name( 'treehouse', 'tree') should returnTrue`.
'''
def check_name(arg1, arg2):
    if arg1 in arg2:
        return True
    else:
        return False

print(check_name('blan', 'blanche'))