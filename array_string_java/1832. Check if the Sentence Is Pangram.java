// A pangram is a sentence where every letter of the English alphabet appears at least once.

// Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

// Example 1:

// Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
// Output: true
// Explanation: sentence contains at least one of every letter of the English alphabet.

class Solution {
    /*
    public boolean checkIfPangram(String sentence) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        
        for (int i=0; i<sentence.length(); i++){            
            char alph = sentence.charAt(i);
            if (map.containsKey(alph)){
                map.put(alph, map.get(alph)+1);
            }
            else {
                map.put(alph, 1);
            }
        }
                
        if (map.size()==26) return true;
        else return false;
        
    }*/
    //HashSet
    public boolean checkIfPangram(String sentence) {
        HashSet<Character> set = new HashSet<Character>();
        for (int i=0; i<sentence.length(); i++){
            set.add(sentence.charAt(i));
        }
        
        return set.size()==26 ? true : false;
    }
}