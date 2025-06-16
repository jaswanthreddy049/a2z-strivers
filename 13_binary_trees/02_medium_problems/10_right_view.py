"""199. Binary Tree Right Side View
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        self.stack=[]
        def res(root,level):
            if not root:return
            if len(self.stack)==level:
                self.stack.append(root.val)
            res(root.right,level+1)
            res(root.left,level+1)
        res(root,0)
        return self.stack


        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        