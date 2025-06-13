"""144. Binary Tree Preorder Traversal
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result=[]
        def pot(node):
            if not node:
                return
            result.append(node.val)
            pot(node.left)
            pot(node.right)
        pot(root)
        return result

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        