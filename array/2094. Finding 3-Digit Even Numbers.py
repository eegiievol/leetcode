'''
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.
'''
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = {}
        le = len(digits)        
        for i in range(le):
            if digits[i]>0:
                num=100*digits[i]
                for j in range(le):
                    if i==j:
                        continue                        
                    num+=(10*digits[j])
                    for k in range(le):
                        if k==i or j==k or digits[k]%2==1:
                            continue
                        num+=digits[k]
                        if num not in ans:
                            ans[num]=1
                        num-=digits[k]
                    num-=(10*digits[j])
        return sorted(ans)
                        