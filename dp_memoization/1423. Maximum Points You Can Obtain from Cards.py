# There are several cards arranged in a row, and each card has an associated number of points. 
# The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. 
# You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def dp(i,j,k):
            if k<=0:
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            mx = max(dp(i+1,j,k-1)+cardPoints[i], dp(i,j-1,k-1)+cardPoints[j])
            mem[(i,j)]=mx
            return mx
            
        mem={}
        return dp(0,len(cardPoints)-1,k)



 