#URL: https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        curr = head
        i = 1
        n = 0
        while curr != None:
            if i == left:
                start_curr = curr
                if left > 1:
                    start_join = prev
            if i == right:
                end_curr = curr
                if curr.next:
                    end_join = curr.next
            prev = curr
            curr = curr.next
            i += 1
            n += 1
        
        prev, next = None, None
        start_curr_cp = start_curr
        while True:
            next = start_curr.next
            start_curr.next = prev
            prev = start_curr
            start_curr = next
            if start_curr == end_curr:
                start_curr.next = prev
                break
        
        if right < n:
            start_curr_cp.next = end_join
        if left > 1:
            start_join.next = end_curr
        if left == 1:
            return start_curr

        return head
        
