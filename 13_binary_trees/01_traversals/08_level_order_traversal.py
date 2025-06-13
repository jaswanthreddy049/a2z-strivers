"""102. Binary Tree Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result=[]
        queue=deque([root])
        while(queue):
            level=[]
            for _ in range(len(queue)):
                value=queue.popleft()
                level.append(value.val)
                if value.left:queue.append(value.left)
                if value.right:queue.append(value.right)
            result.append(level)
        return result



        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        