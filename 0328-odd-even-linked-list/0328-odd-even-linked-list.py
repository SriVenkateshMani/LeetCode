# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_curr = head
        even_curr = head.next
        connect = head.next

        while even_curr and even_curr.next:
            odd_curr.next = even_curr.next
            odd_curr = odd_curr.next
            even_curr.next = odd_curr.next
            even_curr = even_curr.next
            
        odd_curr.next = connect

        return head
