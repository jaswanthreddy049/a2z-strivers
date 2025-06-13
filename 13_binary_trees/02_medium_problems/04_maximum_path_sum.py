"""124. Binary Tree Maximum Path Sum
Solved
Hard
Topics
premium lock icon
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 """
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxi=float('-inf')
        def res(root):
            if not root:return 0
            l=max(0,res(root.left))
            r=max(0,res(root.right))
            self.maxi=max(self.maxi,root.val+l+r)
            return root.val+max(l,r)
        res(root)
        return self.maxi
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        