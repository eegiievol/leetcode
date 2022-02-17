# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

 

# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(node):
            if node == head[node]:
                return node
            head[node] = find(head[node])
            return head[node]
        
        def union(n1, n2):
            r1,r2 = find(n1), find(n2)
            if r1!=r2:
                head[r2]=r1
        
        ans = []
        head = [i for i in range(len(s))]
        for v1,v2 in pairs:
            union(v1,v2)
        
        reg = defaultdict(list)
        for i in range(len(s)):
            reg[find(i)].append(s[i])
            
        for n in reg: #heapify by lex order
            heapify(reg[n])
        
        for i in range(len(s)):
            el = heappop(reg[find(i)])
            ans.append(el)
        return "".join(ans)
