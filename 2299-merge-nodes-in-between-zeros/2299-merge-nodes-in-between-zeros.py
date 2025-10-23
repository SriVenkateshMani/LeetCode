# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        build = head
        curr = build.next
        curr_sum = 0
        while curr:
            if curr.val != 0:
                curr_sum += curr.val
                curr = curr.next
            else:
                build.val = curr_sum
                curr_sum = 0
                build.next = curr.next
                build = build.next
                curr = curr.next
        
        return head