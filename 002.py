''' Python Challenge - 2
Use the function called morse_code. It will take 1 parameter, a word. For example: 'apple'.
Using the given morse code translation, return a single string with the word translated into morse code.
Ex: 'dot-dash-dot-dash-dash-dot-dot-dash-dash-dot-dot-dash-dot-dot-dot'
'''

def morse_code(word):
    morse_dict = {
        'a': 'dot-dash',
        'b': 'dash-dot-dot-dot',
        'c': 'dash-dot-dash-dot',
        'd': 'dash-dot-dot',
        'e': 'dot',
        'f': 'dot-dot-dash-dot',
        'g': 'dash-dash-dot',
        'h': 'dot-dot-dot-dot',
        'i': 'dot-dot',
        'j': 'dot-dash-dash-dash',
        'k': 'dash-dot-dash',
        'l': 'dot-dash-dot-dot',
        'm': 'dash-dash',
        'n': 'dash-dot',
        'o': 'dash-dash-dash',
        'p': 'dot-dash-dash-dot',
        'q': 'dash-dash-dot-dash',
        'r': 'dot-dash-dot',
        's': 'dot-dot-dot',
        't': 'dash',
        'u': 'dot-dot-dash',
        'v': 'dot-dot-dot-dash',
        'w': 'dot-dash-dash',
        'y': 'dash-dot-dash-dash',
        'z': 'dash-dash-dot-dot'
    }
    # enter your code below
    result = ""
    for index, letter in enumerate(word):
        if index == 0:
            result += f"{morse_dict[letter]}"
        else:
            result += f"-{morse_dict[letter]}"

    return result