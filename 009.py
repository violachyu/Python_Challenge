'''Python Challenge - 9
Fix the Pep8 mistakes in the code below.
'''

# There should be two blank lines after imports, funcitons, and classes.
# Delete unnecessary blank space after "[".
# Keep quotations consistent. Single was used before so these strings should also have single quotations.
# There should be a blank line before a method.

# Raw Data
import datetime
def my_func():
    return 'It ran!'
sizes = [ "small", "medium", "large" ]
class Tree:
    def __init__(self, size, characteristics):
        self.size = size
        self.charac = characteristics
        self.roots = True
        self.leaves = 0
    def grow_leaves(self):
        self.leaves += 1
Tree( sizes[ 0 ], { 'name': 'Tulip Tree' } )