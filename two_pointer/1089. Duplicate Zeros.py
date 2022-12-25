class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = 0
        le = len(arr)
        for num in arr:
            if not num:
                zeroes += 1
        j = le + zeroes - 1
        for i in range(le-1, -1, -1):
            if j<le:
                arr[j] = arr[i]
            j-=1
            if arr[i] == 0:
                if j<le:
                    arr[j] = 0
                j-=1
        