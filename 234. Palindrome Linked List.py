#URL: https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TODO: Write your code here
        # Finding Mid
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        #Reversing the List for Comparision
        prev = self.reverseList(slow)

        #Printing The 2 strings
        head1 = head
        head2 = prev
        while head1 != None and head2 != None:
            print(f"Head 1:{head1.val} Head 2:{head2.val}")
            if head1.val != head2.val:
                return False
                break
            head1 = head1.next
            head2 = head2.next
        return True
        
        test = self.reverseList(prev)
        test_head = head
        while test_head != None:
            print(f"Final List:{test_head.val}")
            test_head = test_head.next
    
    def reverseList(self, slow):
        prev = None
        while slow != None:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        return prev
