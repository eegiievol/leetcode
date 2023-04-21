'''
Medium
6.4K
136
company
Bloomberg
company
Amazon
company
Apple
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        heap = [intervals[0][1]]
        rooms = 1
        for start,end in intervals[1:]:
            if heap[0] <= start:    #heap peek
                heappop(heap) 
            else:
                rooms += 1
            heappush(heap, end)

        return rooms
