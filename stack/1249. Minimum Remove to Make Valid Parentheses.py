# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []        
        ans = []        
        ctr=0
        for i,val in enumerate(s):
            if val=='(':
                stack.append(ctr)                
            elif val==')':
                if not stack:
                    continue
                else:
                    stack.pop()
            ans.append(val) 
            ctr+=1
        
        while stack:
            removed = stack.pop()
            ans.pop(removed)
        return "".join(ans)
        
