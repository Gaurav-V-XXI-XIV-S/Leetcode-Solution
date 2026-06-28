# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        cur=slow.next
        slow.next=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt

        first=head
        second=prev
        while second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2