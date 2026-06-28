# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        cur = head

        while cur:
            prev = dummy

            # find position
            while prev.next and prev.next.val < cur.val:
                prev = prev.next

            nxt = cur.next
            cur.next = prev.next
            prev.next = cur

            cur = nxt

        return dummy.next