# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

class Solution:    
    def alienOrder(self, words: List[str]) -> str:       
        def topologicalSort(q):
            ans = []
            while q:
                popped=q.popleft()
                ans.append(popped)
                for nei in adj_list[popped]:
                    incoming[nei]-=1
                    if incoming[nei]==0:
                        q.append(nei) 
            return "".join(ans) if len(ans)==len(incoming) else ""
        
        incoming = {ch:0 for word in words for ch in word}
        adj_list = defaultdict(list)
        
        for first,second in zip(words, words[1:]):
            for src,dest in zip(first, second):
                if src!=dest:
                    if dest not in adj_list[src]:
                        adj_list[src].append(dest)
                        incoming[dest]+=1
                    break
            else:
                if len(first)>len(second):
                    return ""        
        q=deque()
        for node in incoming:
            if incoming[node]==0:
                q.append(node)     
        return topologicalSort(q)
