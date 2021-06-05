'''Python Challenge - 4
Create a function called reverse. It will take 1 parameter, a string. For example: 'treehouse'
Your function will need to reverse the string and return it. For example: 'esuoheert'.
'''

def reverse(word):
    letter_list = []
    for i in word:
        letter_list.append(i)

    result_list = []
    for letter in letter_list:
        result_list.insert(0, letter)
    result = ''.join(result_list)
    return result

print(reverse('icecream'))