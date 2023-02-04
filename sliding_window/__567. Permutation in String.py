'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        reg = collections.Counter(s1)
        le = len(reg)
        
        cur = {}
        j = 0
        ctr = 0
        for i,ch in enumerate(s2):
            cur[ch] = cur.get(ch, 0) + 1
            
            #if moved i resulter ctr++
            if cur[ch] == reg[ch]: 
                ctr += 1

            #j out of position, move j forward
            if i-j >= len(s1):
                cur[s2[j]] -= 1

                #moved j resulted ctr--
                if cur[s2[j]] == reg[s2[j]] - 1:
                    ctr -= 1
                j+=1
            if ctr == le:
                return True

        return False
