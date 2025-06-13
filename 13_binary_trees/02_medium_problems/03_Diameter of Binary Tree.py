"""543. Diameter of Binary Tree
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 """
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxi=0
        def res(root):
            if not root:return 0
            l=res(root.left)
            r=res(root.right)
            self.maxi=max(self.maxi,l+r)
            return max(l,r)+1
        res(root)
        return self.maxi
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        