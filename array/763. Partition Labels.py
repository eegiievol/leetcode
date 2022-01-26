# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        ctr = Counter(s)
        ans = []
        cur = []
        last = -1
        
        for i, val in enumerate(s):
            if val not in cur:
                cur.append(val)
            ctr[val]-=1
            if ctr[val]==0:
                cur.remove(val)
            if not cur:
                ans.append(i-last)
                last = i
        
        return ans
