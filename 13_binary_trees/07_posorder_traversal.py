"""145. Binary Tree Postorder Traversal
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result=[]
        def pot(node):
            if not node:
                return
            pot(node.left)
            pot(node.right)
            result.append(node.val)
        pot(root)
        return result
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        