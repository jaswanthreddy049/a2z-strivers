"""25. Reverse Nodes in k-Group
Solved
Hard
Topics
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        def reverse(temp):
            prev=None
            while(temp):
                nst=temp.next
                temp.next=prev
                prev=temp
                temp=nst
            return prev
        def findkthnode(temp,k):
            while(temp and k>0):
                temp=temp.next
                k-=1
            return temp
        temp=head
        prevnode=None
        while(temp):
            kthnode=findkthnode(temp,k-1)
            if kthnode is None:
                if prevnode:
                    prevnode.next=temp
                break
            nextnode=kthnode.next
            kthnode.next=None
            revhead=reverse(temp)
            if temp==head:
                head=revhead
            else:
                prevnode.next=revhead
            prevnode=temp
            temp=nextnode
        return head


        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        