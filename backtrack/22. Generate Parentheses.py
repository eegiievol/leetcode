# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(opening, closing, arr):
            if opening==0 and closing==0:
                ans.append("".join(arr))
                return 
                        
            if opening>0:
                arr.append('(')
                backtrack(opening-1, closing, arr)
                arr.pop()
            if closing>0 and closing>opening:
                arr.append(')')
                backtrack(opening, closing-1, arr)
                arr.pop()
        ans = []
        backtrack(n, n, [])
        return ans
