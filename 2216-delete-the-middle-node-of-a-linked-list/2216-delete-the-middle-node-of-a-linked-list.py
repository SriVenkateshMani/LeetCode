# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        mid_idx = length // 2

        # remove the mid val
        i = -1
        dummy = ListNode(0, head)
        prev = dummy
        curr1 = head

        while curr1:
            i += 1
            if i == mid_idx:
                prev.next = curr1.next
                curr1 = curr1.next
            else:
                prev = prev.next
                curr1 = curr1.next
        
        return dummy.next