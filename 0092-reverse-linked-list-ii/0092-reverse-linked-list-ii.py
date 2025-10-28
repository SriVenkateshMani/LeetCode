# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_prev = dummy
        curr = head

        i = 0
        while i < left - 1:
            left_prev = curr
            curr = curr.next
            i += 1

        prev = None
        i = 0
        while i < right - left + 1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next