# Given a file and assume that you can only read the file using a given 
# method read4, implement a method read to read n characters. 
# Your method read may be called multiple times.

################################ Method read4: ################################

# The API read4 reads four consecutive characters from file, then writes 
# those characters into the buffer array buf4.

# The return value is the number of actual characters read.

# Note that read4() has its own file pointer, much like FILE *fp in C.

################################# Definition of read4: ################################

#     Parameter:  char[] buf4
#     Returns:    int

# buf4[] is a destination, not a source. The results from 
# read4 will be copied to buf4[].

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

################################# Method read: ################################

# By using the read4 method, implement the method read that reads n 
# characters from file and store it in the buffer array buf. Consider 
# that you cannot manipulate file directly.

# The return value is the number of actual characters read.




################################## Example 1:#################################
# Input: file = "abc", queries = [1,2,1]
# Output: [1,2,0]
# Explanation: The test case represents the following scenario:
# File file("abc");
# Solution sol;
# sol.read(buf, 1); // After calling your read method, buf should contain "a". 
# We read a total of 1 character from the file, so return 1.
# sol.read(buf, 2); // Now buf should contain "bc". We read a total of 
# 2 characters from the file, so return 2.
# sol.read(buf, 1); // We have reached the end of file, no more characters 
# can be read. So return 0.
# Assume buf is allocated and guaranteed to have enough space for storing 
# all characters from the file.

class Solution:   
    
    def __init__(self):
        self.q=[]*4 #cache
        self.size = 0 #cache data size
        
    def read(self, buf: List[str], n: int) -> int: 
        copied = 0           
        if n<=self.size:   #cache has enough data         
            buf[:n:] = self.q[:n:]
            self.q[::]=self.q[n:5:] #rotate cache
            self.size-=n            
            return n
        else:  #cache has not enough data        
            buf[:self.size:] = self.q[:self.size:]  #emptying cache
            n-=self.size            
            copied = self.size
            self.size = 0
        
        #we need to read from file
        buf4 = ['']*4
        while n>0:            
            required = 4 if n>=4 else n
            got=read4(buf4)            
            if got<required: #EOF
                buf[copied:copied+got:] = buf4[0:got:]
                return copied+got
            elif got>required: #this case, copy leftover data to cache
                buf[copied:copied+required:] = buf4[0:required:]
                self.q[::] = buf4[required:got+1:]
                self.size = got-required                
                return copied+required
            else: #we got exactly what we needed from file
                buf[copied:copied+got:] = buf4[0:got:]
                copied+=got
                n-=got

        return copied
                

                
                
                
                
                
                
                
                