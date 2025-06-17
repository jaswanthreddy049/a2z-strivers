"""863. All Nodes Distance K in Binary Tree
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        my=defaultdict(list)
        def res(node,parent):
            if not node:return
            if parent:
                my[node].append(parent)
                my[parent].append(node)
            if node.left:
                res(node.left,node)
            if node.right:
                res(node.right,node)
        res(root,None)
        queue=deque([(target,0)])
        visited=set()
        result=[]
        while(queue):
            node,dis=queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if dis==k:
                result.append(node.val)
            elif dis<k:
                for i in my[node]:
                    if i not in visited:
                        queue.append([i,dis+1])
        return result

        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        