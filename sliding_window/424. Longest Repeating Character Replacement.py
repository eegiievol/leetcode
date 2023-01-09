'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        occur = {}
        j = 0
        ans = 0
        for i,ch in enumerate(s):
            occur[ch] = occur.get(ch, 0) + 1
            
            #max based on dictionary value
            while i-j+1 - occur[max(occur, key=occur.get)]>k:
                occur[s[j]] -= 1
                if occur[s[j]]==0:
                    del occur[s[j]]
                j+=1
            ans = max(ans, i-j+1)
        return ans
