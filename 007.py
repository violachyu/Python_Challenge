'''Python Challenge - 7
Take a look at the example data structure below. Create a function called breeds.
It will receive 1 parameter, a data structure like the one below.
Return a list of all the pet breeds a person has.
For example, using the data structure below, the function should return ['American Shorthair', 'Pitbull'].
'''

# {
#     'name': 'Javier Hernandez',
#     'pets': [
#         {
#             'name': 'Kitty',
#             'breed': 'American Shorthair'
#         },
#         {
#             'name': 'Buzz',
#             'breed': 'Pitbull'
#         }
#     ],
#     'classes': ('Math', 'Science', 'Art')
# }
# enter your code below

def breeds(person):
    result = []
    for item in person['pets']:
        result.append(item['breed'])

    return result

javier = {
    'name': 'Javier Hernandez',
    'pets': [
        {
            'name': 'Kitty',
            'breed': 'American Shorthair'
        },
        {
            'name': 'Buzz',
            'breed': 'Pitbull'
        }
    ],
    'classes': ('Math', 'Science', 'Art')
}

print(breeds(javier))

