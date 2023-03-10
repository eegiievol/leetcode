'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True 
'''

class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False    # is leaf

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TreeNode()
            cur = cur.children[ch]
        cur.end = True
    
    def __helper(self, node, word, i):
        if i>=len(word):
            if node.end:
                return True
            else:
                return False
        
        if word[i] == '.':
            for child in node.children:
                if self.__helper(node.children[child], word, i+1):
                    return True
        else:
            if word[i] in node.children:
                return self.__helper(node.children[word[i]], word, i+1)
        
        return False

    def search(self, word: str) -> bool:
        return self.__helper(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)