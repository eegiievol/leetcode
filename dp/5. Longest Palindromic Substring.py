'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        le = len(s)
        dp = [[False]*le for _ in range(le)]
        for i in range(le):
            dp[i][i] = True
        ans = s[0]

        for i in range(le-2, -1, -1):
            for j in range(i+1, le):
                if s[i]==s[j]:
                    if i+1==j or dp[i+1][j-1]:
                        dp[i][j] = True
                        ans = max(s[i:j+1], ans, key=len)
        
        return ans
