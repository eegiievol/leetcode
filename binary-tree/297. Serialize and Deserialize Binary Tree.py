'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
'''
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            popped = q.popleft()
            if popped:  #if node exist, we always add its children to 'q'
                ans.append(str(popped.val))
                q.append(popped.left)
                q.append(popped.right)
            else:   #means it is a child of non-empty node
                ans.append('null')

        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        arr = data.split(',')
        q = collections.deque()

        root = TreeNode(arr[0])
        q.append(root)
        i = 1
       
        while q:
            popped = q.popleft()
            if popped:
                if arr[i] != 'null':
                    popped.left = TreeNode(int(arr[i]))
                if arr[i+1] != 'null':
                    popped.right = TreeNode(int(arr[i+1]))
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                i = i + 2
        
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))