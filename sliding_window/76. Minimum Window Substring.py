'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        match = Counter(t)
        occur = {}
        j = 0
        ctr = 0 #matching characters
        ans = (float('inf'), 0, 0)

        for i, ch in enumerate(s):
            occur[ch] = occur.get(ch, 0) + 1
            if occur[ch] == match.get(ch, 0):
                ctr += 1
            while ctr==len(match): #shrink while 'ctr' condition meet
                if i-j+1<ans[0]:
                    ans = (i-j+1, j, i)
                occur[s[j]] -= 1
                if occur[s[j]]<match[s[j]]:
                    ctr -= 1
                j += 1
            
        
        return s[ans[1]:ans[2]+1] if ans[0] != float('inf') else ""



