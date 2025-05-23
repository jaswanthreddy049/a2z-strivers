"""Remove duplicated from sorted DLL
100
Hard
Hint
"""
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        cur=head
        freq={}
        temp=None
        while(cur):
            if cur.val in freq:
                while(cur.val==temp.val):
                    cur=cur.next
                temp.next=cur
                cur.prev=temp
            else:
                temp=cur
                freq[cur.val]=1
                cur=cur.next
        return head
