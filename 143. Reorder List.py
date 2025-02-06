# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # TODO: Write your code here
        slow, fast = head, head
        prev = None
        if not fast.next:
            return
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = self.reverse(slow)
        while  head2.next:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next 
        #head1.next = None

    def reverse(self, slow):
        prev = None
        while slow != None:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        return prev
        
