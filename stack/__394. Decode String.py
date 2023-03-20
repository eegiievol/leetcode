'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 
 '''
 class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for ch in s:
            if ch == ']':
                
                #capture chars in parenthesis
                cur = ''
                while True:
                    popped = stack.pop()
                    if popped == '[':
                        break
                    cur += popped

                #capture numbers
                num_str = ''
                while stack and stack[-1].isnumeric():
                    num_str += stack.pop()
                num = int(num_str[::-1])
                
                #push back to stack
                for _ in range(num):
                    for cur_ch in cur[::-1]:
                        stack.append(cur_ch)
            else:
                stack.append(ch)
        
        return "".join(stack)
