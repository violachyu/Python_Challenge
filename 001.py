'''Python Challenge - 1
Create a function called splitsville. It will take 1 parameter, an address. For example: '100 E Main St, Anywhereville, Oregon, 22222'.
Split the string into the street, city, state, and zip.
Return a dictionary with the keys street, city, state, zip_code and the values from the split string. Example: {'street': '100 E Main St', etc.}
'''
def splitsville(address):
    value_list = address.split(', ')
    key_list = ['street','city', 'state', 'zip_code']

    return dict(zip(key_list, value_list))
# Ref: https://stackoverflow.com/questions/209840/how-do-i-convert-two-lists-into-a-dictionary

splitsville('100 E Main St, Anywhereville, Oregon, 22222')
