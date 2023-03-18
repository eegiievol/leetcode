'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
        def union(n1,n2):
            r1,r2 = find(n1), find(n2)
            if r1!=r2:
                root[r1] = root[r2]

        if not nums:
            return 0
        #remove duplicates        
        reg = set(nums)
        #union find
        root = {}
        for num in reg:
            root[num] = num
        for num in reg:
            if num-1 in reg:
                union(num, num-1)
        #ans
        ctr = {}
        for num in reg:
            r = find(num)
            ctr[r] = ctr.get(r, 0) + 1
        
        return max(ctr.values())

