# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        first_cp = 0
        prev_cp = 0
        curr_cp = 0
        min_dist = float("inf")
        prev = head
        curr = prev.next
        fow = curr.next
        pos = 1

        while fow:
            if (prev.val < curr.val and fow.val < curr.val) or (prev.val > curr.val and fow.val > curr.val):
                curr_cp = pos
                if first_cp == 0:
                    first_cp = curr_cp
                if prev_cp != 0:
                    min_dist = min(min_dist, curr_cp - prev_cp)
            
                prev_cp = curr_cp

            prev = curr
            curr = fow
            fow = fow.next
            pos += 1

        if curr_cp != 0 and first_cp != 0 and first_cp != curr_cp:
            max_dist = curr_cp - first_cp
            res[1] = max_dist

        if min_dist != float("inf"):
            res[0] = min_dist
        
        return res
        