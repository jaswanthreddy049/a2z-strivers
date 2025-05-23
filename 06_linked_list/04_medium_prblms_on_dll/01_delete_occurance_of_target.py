"""Given the head of a doubly linked list and an integer target. Delete all nodes in the linked list with the value target and return the head of the modified linked list.


Examples:
Input: head -> 1 <-> 2 <-> 3 <-> 1 <-> 4, target = 1

Output: head -> 2 <-> 3 <-> 4

Explanation: All nodes with the value 1 were removed.

Input: head -> 2 <-> 3 <-> -1 <-> 4 <-> 2, target = 2

Output: head -> 3 <-> -1 <-> 4

Explanation: All nodes with the value 2 were removed.

Note that the value of head is changed."""
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        cur=head
        while(cur):
            if cur.val==target:
                if cur.prev:
                    cur.prev.next=cur.next
                else:head=cur.next
                if cur.next:
                    cur.next.prev=cur.prev
            cur=cur.next
        return head
            