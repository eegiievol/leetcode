# 1128. Number of Equivalent Domino Pairs
# Easy

# 437

# 215

# Add to List

# Share
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        hm = {}
        for a,b in dominoes:
            if a>b:
                hm[(b,a)] = hm.get((b,a), 0)+1
            else:
                hm[(a,b)] = hm.get((a,b), 0)+1
        
        ans = 0
        for pair in hm:
            if hm[pair]>1:
                n = (hm[pair])
                ans += (n*(n-1)//2)
        return ans
