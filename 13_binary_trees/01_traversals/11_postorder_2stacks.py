# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result=[]
        stack=[root]
        while(stack):
            if not root:
                return []
            node=stack.pop()
            result.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        final=[]
        while(result):
            node=result.pop()
            final.append(node.val)
        return final


        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        