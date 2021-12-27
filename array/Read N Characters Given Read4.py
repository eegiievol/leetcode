"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):        
        buf4 = ['']*4
        cur=0
        #print(buf)
        
        while n>0:
            required = 4 if n>=4 else n            
            num = read4(buf4)  
            
            if num<required: #FILE EOF
                buf[cur:cur+num]=buf4[0:num]                
                return cur+num   
            else:
                buf[cur:cur+required]=buf4[0:required]  
                cur+=required            
                n-=required
        print(cur)
        return cur
        
            
            
            