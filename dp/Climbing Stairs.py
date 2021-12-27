class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(mem, n):
            
            if n<=2:
                return n
            
            if n in mem:
                return mem[n]
        
            steps = helper(mem, n-1)+helper(mem, n-2)
            mem[n] = steps
            return steps
        
        
        mem={}
        return helper(mem, n)
        