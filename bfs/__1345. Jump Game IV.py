'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
'''

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        le = len(arr)
        if le <= 1:
            return 0

        neighbors = {}
        for i in range(le):
            if arr[i] in neighbors:
                neighbors[arr[i]].append(i)
            else:
                neighbors[arr[i]] = [i]
        
        q = collections.deque()
        visited = {0}
        
        q.append(0)

        steps = 0
        while q:
            for _ in range(len(q)):
                popped = q.popleft()
                if popped == le - 1:
                    return steps

                for nei in neighbors[arr[popped]]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

                # clear the list to prevent redundant search
                neighbors[arr[popped]].clear()

                if popped-1>=0 and popped-1 not in visited:
                    visited.add(popped-1)
                    q.append(popped-1)
                if popped+1<le and popped+1 not in visited:
                    visited.add(popped+1)
                    q.append(popped+1)

            steps += 1

        return -1
