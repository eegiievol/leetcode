class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(dct, n):
            
            if n==0:
                return 0
            if n<=2:
                return 1
            
            if n in dct:
                return dct[n]
        
            ans = helper(dct, n-3)+helper(dct, n-2)+helper(dct, n-1)
            dct[n] = ans
            return ans

        dc = {}
        return helper(dc, n)

