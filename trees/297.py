# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ""
        # Approach - convert to preorder and inorder and concatenate them together and then use that for deserialize

        def _preorder (curr):
            nonlocal result
            if not curr:
                result += "N,"
                return
            result += str(curr.val) + ","
            _preorder(curr.left)
            _preorder(curr.right)
        
        _preorder(root)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = list(data.split(',')[:-1])
        self.i = 0

        def dfs():
            if preorder[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(preorder[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))