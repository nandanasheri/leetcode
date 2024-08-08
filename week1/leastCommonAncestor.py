# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        Was sort of stuck but you just need to find a pattern - if both values are to the same side of a node, then that is NOT the least common ancestor 
        so you keep going left and right accordingly simple iterative function o(n) since you would need to loop through the whole tree
        '''
        curr = root
        while (curr != None):
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
        return None
        