// Write a function that reverses a string. The input string is given as an array of characters s.

// You must do this by modifying the input array in-place with O(1) extra memory.

 

// Example 1:

// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]

//test purpose

class Solution {
    
    public void helper(char[] s, int l, int r){
        if (l>=r) return;
        
        char tmp = s[l];
        s[l++] = s[r];
        s[r--] = tmp;
        helper(s, l, r);
    }
    
    public void reverseString(char[] s) {
        helper(s, 0, s.length-1);
    }
}
