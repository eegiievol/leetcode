# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].

class Solution(object):
    def findLength(self, A, B):        
        lena=len(A)
        lenb=len(B)
        
        mem = [[0]*(lenb+1) for _ in range(lena+1)]
        
        for i in range(lena-1,-1,-1):
            for j in range(lenb-1,-1,-1):
                if A[i]==B[j]:
                    mem[i][j]=mem[i+1][j+1]+1
        return max([max(i) for i in mem])
        