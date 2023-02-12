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
import collections
class Solution:
    def longestPalindrome(self, s: str) -> str:
        le = len(s)
        dp = [[0] * le for _ in range(le)]
        for i in range(le):
            dp[i][i] = 1
        

        ans = s[0]
        for i in range(le-2, -1, -1):
            for j in range(i, le):
                if s[i]==s[j]:
                    if i+1>=j or dp[i+1][j-1]:
                        dp[i][j] = 1
                        ans = max(ans, s[i:j+1], key=len)
        return ans


