"""94. Binary Tree Inorder Traversal
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        def iot(node):
            if not node:
                return
            iot(node.left)
            result.append(node.val)
            iot(node.right)
        iot(root)
        return result
        
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        