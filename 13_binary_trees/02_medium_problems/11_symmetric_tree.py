"""101. Symmetric Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def res(t1,t2):
            if not t1 and not t2 :return True
            if not t1 or not t2:return False
            if t1.val==t2.val and res(t1.left,t2.right) and res(t1.right,t2.left):
                return True
            return False
        return res(root,root)
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        