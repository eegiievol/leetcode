# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        hm = {}
        ans=[]
        for l in range(len(s)-9):
            sub = s[l:l+10]
            hm[sub] = hm.get(sub, 0)+1
    
        for sub in hm:
            if hm[sub]>1:
                ans.append(sub)
        return ans