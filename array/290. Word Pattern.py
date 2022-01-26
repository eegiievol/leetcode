# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:        
        hm = {}
        uniq = {}
        ls = s.split()
        if len(pattern)!=len(ls):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in hm:
                hm[pattern[i]]=ls[i]
                if ls[i] not in uniq:
                    uniq[ls[i]]=1
                else:
                    return False
                
            elif hm[pattern[i]]!=ls[i]:
                return False
                
        
        return True