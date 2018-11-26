#checks and returns all anagrams of a word from a list of words

def anagrams(word, words):
    
    ag = []
    for w in words:
        list_w = list(w)
        list_w.sort()
        list_wrd = list(word)
        list_wrd.sort()
        
        if list_w == list_wrd:
            ag.append(w)
            
    return ag
