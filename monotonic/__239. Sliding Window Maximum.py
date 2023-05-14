# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k=3
        # nums         1,  3,  -1, -3,  5,  3,  6,  7
        # window                           [        ]

        # deque       [7]
        # ans         [3, 3, 5, 5, 6, 7]


        def insert(i):
            if q and i-q[0] == k:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

        q = deque()
        ans = []

        for i in range(k):
            insert(i)
        ans.append(max(nums[:k]))

        for i in range(k, len(nums)):
            insert(i)
            ans.append(nums[q[0]])

        return ans

