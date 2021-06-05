'''Python Challenge - 3
Create a function called pop. It will take 2 parameters, a list and an index. For example: [1,2,3], 1
Your function will need to make sure the index is in the list's range
and then remove the element at that index. Then return the list.
For example, [1,2,3], 1 would return [1,3]. If the element is not in range,
then an IndexError will occur and an error message 'Invalid Index' should be returned instead.
'''

def pop(sample_list, number):
    try:
        if sample_list[number] in sample_list:
            sample_list.remove(sample_list[number])
        else:
            raise IndexError
    except IndexError:
        return "Invalid Index"
    return sample_list

print(pop([1,2,3], 5))