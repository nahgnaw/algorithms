# -*- coding: utf-8 -*-


"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def _serialize(node):
            if node:
                tree_list.append(str(node.val))
                _serialize(node.left)
                _serialize(node.right)
            else:
                tree_list.append('#')

        tree_list = []
        _serialize(root)
        return ' '.join(tree_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def _deserialize():
            val = next(tree_list)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = _deserialize()
            node.right = _deserialize()
            return node

        tree_list = iter(data.spilit())
        return _deserialize()

    def serialize2(self, root):
        import json
        def _serialize(node):
            if node:
                return (node.val, _serialize(node.left), _serialize(node.right))
            return None
        return json.dumps(_serialize(root))

    def deserialize2(self, data):
        import json
        def _deserialize(t):
            if t:
                node = TreeNode(t[0])
                node.left = _deserialize(t[1])
                node.right = _deserialize(t[2])
                return node
        return _deserialize(json.loads(data))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))