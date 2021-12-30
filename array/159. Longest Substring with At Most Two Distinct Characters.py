# Given a string s, return the length of the longest substring that contains at most two distinct characters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        first,last = 0,0
        le = len(s)
        tracker = {}
        
        while last<le:
            tracker[s[last]] = tracker.get(s[last], 0) + 1
            while len(tracker)>2:
                tracker[s[first]]-=1
                if tracker[s[first]]==0:
                    del tracker[s[first]] 
                first+=1
            ans = max(ans, last-first+1)
            last+=1
            
        return ans


