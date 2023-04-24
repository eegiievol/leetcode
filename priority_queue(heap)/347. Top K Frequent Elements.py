class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []        
        freq = {}
        
        #number frequency
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        
        #tuple = (ctr, num)
        #maxheap minus value trick
        
        #heappop(heap), heappush(heap, (ctr, num))
        for el, count in freq.items():
            heappush(heap, -count, el))

        #here
            
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        
        return ans
            
        
        
        
