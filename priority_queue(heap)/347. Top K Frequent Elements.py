class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        heap = []
        for num in ctr:
            heappush(heap, (-ctr[num], num))
        
        return [heappop(heap)[1] for _ in range(k)]
        
