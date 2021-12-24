# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
# such that every character in t (including duplicates) is included in the window. If there is no such substring, 
# return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
 
class Solution:
    def minWindow(self, s: str, t: str) -> str:  
        dct_t = Counter(t)  #window char track in str t
        uniq_cnt=len(dct_t) # unique char count        
        ans = [""] 
        uniq_win = 0    # satisfied uniq char count in window
        window = {}   #window char track in window
        sle=len(s)        
        l,r=0,0
        
        while r<sle:
            ch = s[r]            
            if ch not in dct_t:
                r+=1
                continue                
            window[ch] = window.get(ch, 0)+1                
            if window[ch]==dct_t[ch]:
                uniq_win += 1            
            
            while l<=r and uniq_win==uniq_cnt:  
                ch = s[l]
                if ch not in dct_t:
                    l+=1
                    continue                
                if window[ch]>dct_t[ch]:  #if [l] has space to move forward
                    window[ch]-=1
                else:                        
                    if len(ans)==1: #
                        ans.append(s[l:r+1])
                    else:
                        if len(s[l:r+1]) < len(ans[1]):
                            ans[1] = s[l:r+1]
                    break                    
                l+=1                
            r+=1
            
        return ans[0] if len(ans)==1 else ans[1]
            
        
        
            
