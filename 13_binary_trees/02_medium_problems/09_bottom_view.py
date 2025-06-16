# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        mydict={}
        queue=deque([(root,0)])
        minlen,maxlen=0,0
        while(queue):
            if not root:return []
            node,col=queue.popleft()
            minlen=min(minlen,col)
            maxlen=max(maxlen,col)
            mydict[col]=node.val
            if node.left:
                queue.append([node.left,col-1])
            if node.right:
                queue.append([node.right,col+1])
        stack=[]
        for i in range(minlen,maxlen+1):
            stack.append(mydict[i])
        return stack


        

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        