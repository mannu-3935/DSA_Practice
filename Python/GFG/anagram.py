# anagrams if they contain the same characters with exactly the same frequencies, regardless of their order
'''
s1 = "geeks" s2 = "kseeg"   -->True
s1 = "allergy", s2 = "allergyy" -->False
s1 = "listen", s2 = "silent" -->True
s1 = "listen", s2 = "lists" -->False
'''
def are_anagrams(s1, s2):
    if len(s1) != len(s2):      #Check if lengths are equal
        return False
    
    # freq1 = [0] * 26                         #---->list for numbers
    # freq2 = [0] * 26
    freq1 = {}                                 #---->dictionary for characters               
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for i in s2:
        if i in freq1:
            freq1[i] -=1
        else:
            return False
    for count in freq1.values():
        if count != 0:
            return False
    return True
    
    '''
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    
    for ch in freq1:
        if freq1[ch] != freq2[ch] or ch not in freq2:
            return False
        
    return True
    '''

    # return freq1 == freq2

s1 = "listen"
s2 = "silent"
print(are_anagrams(s1.lower(), s2.lower()))