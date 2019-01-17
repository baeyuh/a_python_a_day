#Find longest sequence of zeros in binary representation of an integer.

def solution(N):
    bin = "{0:b}".format(N)
    bin = bin.strip('0')
    
    if '0' in bin:
        bin_split = bin.split('1')
        gp = []
        for i in bin_split:
            gaps = []
            if '0' in i:
                gaps.append(i)
            else:
                gaps.append('')
            gp = gp + gaps   
        gap_len = [len(g) for g in gp if g!='']
        return max(gap_len)
        
    else:
        return 0
