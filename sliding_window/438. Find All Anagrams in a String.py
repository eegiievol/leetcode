'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mem = collections.Counter(p)

        j = 0
        ctr = 0
        cur = {}
        ans = []
        for i,ch in enumerate(s):
            cur[ch] = cur.get(ch, 0) + 1
            
            #i just caused ctr to increment
            if mem[ch]==cur[ch]:
                ctr += 1
                
            #j out of position, move j forward
            if i-j >= len(p):
                cur[s[j]] -= 1
                
                #j just caused ctr to decrement
                if cur[s[j]] == mem[s[j]]-1:
                    ctr -= 1
                j+=1
            #final check
            if ctr == len(mem):
                ans.append(j)
        
        return ans
