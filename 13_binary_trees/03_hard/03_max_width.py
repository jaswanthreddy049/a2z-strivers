"""662. Maximum Width of Binary Tree
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        queue=deque([(root,0)])
        ans=0
        while(len(queue)>0):
            first=queue[0][1]
            last=queue[len(queue)-1][1]
            ans=max(ans,last+1-first)
            new=deque()
            for _ in range(len(queue)):
                node,pos=queue.popleft()
                if node.left:
                    new.append((node.left,pos*2))
                if node.right:
                    new.append((node.right,pos*2+1))
            queue=new
        return ans



        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        