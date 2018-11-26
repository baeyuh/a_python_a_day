#split strings by index splicing 

def solution(s):
    if len(s) % 2 == 0:
        return list(s[i:i+2] for i in range(0, len(s), 2))
        
    if len(s) % 2 != 0:
        s_ = s + '_'
        return list(s_[i:i+2] for i in range(0, len(s_), 2))
