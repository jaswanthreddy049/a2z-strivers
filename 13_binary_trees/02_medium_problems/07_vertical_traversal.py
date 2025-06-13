"""987. Vertical Order Traversal of a Binary Tree
Solved
Hard
Topics
premium lock icon
Companies
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

"""# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        mydict=defaultdict(list)
        queue=deque([(root,0,0)])
        while(queue):
            if not root :return []
            node,row,col=queue.popleft()
            mydict[col].append([row,node.val])
            if node.left:queue.append([node.left,row+1,col-1])
            if node.right:queue.append([node.right,row+1,col+1])
        result=[]
        for i in sorted(mydict):
            value=sorted(mydict[i], key=lambda x:(x[0],x[1]))
            result.append([val for row,val in value])
        return result

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        