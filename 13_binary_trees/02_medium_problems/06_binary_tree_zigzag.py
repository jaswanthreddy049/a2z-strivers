"""103. Binary Tree Zigzag Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        def res(root):
            stack=deque([root])
            result=[]
            direction=True
            if not root:return []
            while(stack):
                value=[]
                for _ in range(len(stack)):
                    node=stack.popleft()
                    value.append(node.val)
                    if node.left:stack.append(node.left)
                    if node.right:stack.append(node.right)
                if direction:
                    result.append(value)
                else:
                    value.reverse()
                    result.append(value)
                direction= not direction
            return result
        return res(root)

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        