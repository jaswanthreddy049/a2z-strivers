"""
Code
Testcase
Testcase
Test Result
110. Balanced Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def res(root):
            if not root:return 0
            l=res(root.left)
            if l==-1:return -1
            r=res(root.right)
            if r==-1:return -1
            if abs(l-r)>1:
                return -1
            return max(l,r)+1
        return res(root)!=-1     
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        