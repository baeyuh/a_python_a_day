#output a list of permutations (no duplicates) of an input string

import itertools

def permutations(string):
    perms = itertools.permutations(string)
    
    lst = []
    
    for p in perms:
        str = ''.join(p)
        lst.append(str)
    
    return set(lst)
