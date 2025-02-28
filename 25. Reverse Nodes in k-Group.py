#URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupTail = dummy
        groupStart = dummy.next
        groupPrev = dummy
        while True:
            groupTail = self.Kthelement(groupTail, k)
            if groupTail == None:
                break
            groupNext = groupTail.next
            prev = None
            curr = groupStart
            while curr != groupNext:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            groupPrev.next = groupTail
            groupStart.next = groupNext
            groupPrev = groupStart
            groupTail = groupStart
            groupStart = groupStart.next
            
        
        return dummy.next


    

    def Kthelement(self, curr, k):
        i = 0
        while i < k and curr != None:
            curr = curr.next
            i += 1
        return curr

