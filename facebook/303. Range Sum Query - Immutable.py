class NumArray:
    arr=[]
    def __init__(self, nums: List[int]):
        summ=0
        self.arr = []
        for i in range(len(nums)):
            summ+=nums[i]
            self.arr.append(summ)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.arr[right]  
        else:
            return self.arr[right]-self.arr[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
