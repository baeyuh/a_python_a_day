#Find the missing element in a given permutation.

#Time complexity: O(n**2) 
def solution(A):
    
    for n in iter(range(100000)):
        for a in iter(range(1, n+1)):
            if a in A:
                continue
            else:
                return a
                
#Time complexity: O(n**2) - slightly better performance
def solution(A):

    a_range = [n+1 for n in range(100000)]
        
    for a in a_range:
        if a in A:
            continue
        else:
            return a
            


