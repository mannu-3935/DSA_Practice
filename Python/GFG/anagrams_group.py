# Group Anagrams Together
'''
Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]

Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
'''

def group_anagrams(words):
    # frequency key approach as in previous anagram checker
    groups = {}
    for w in words:
        #dict of char counts for one word, e.g. {'a':2, 'b':1}
        freq  ={}
        for ch in w:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # freq.items() → view of key-value pairs: [('a',2), ('b',1)]
        key = tuple(sorted(freq.items()))
        if key in groups:
            groups[key].append(w)
        else:
            groups[key] = [w]

    return list(groups.values())


arr1 = ["act", "god", "cat", "dog", "tac"]
print(group_anagrams(arr1))  # [["act","cat","tac"],["god","dog"]]

arr2 = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
print(group_anagrams(arr2)) # [["abc","cab","bac"],["listen","silent","enlist"],["rat","tar","art"]]