# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next

        r = k % l
        if r == 0:
            return head
            
        curr1 = head
        i = 0
        while i < l-r-1:
            curr1 = curr1.next
            i += 1

        temp = curr1.next
        curr1.next = None

        tail = temp
        while tail:
            if tail.next == None:
                tail.next = head
                return temp
            else:
                tail = tail.next
        
        #return temp