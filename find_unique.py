#finding unique number from a list of numbers by using Counter and accessing dictionary values

from collections import Counter

def find_uniq(arr):
    count = Counter(arr)
    
    for k, n in count.items():
        if n == 1:
            return k
