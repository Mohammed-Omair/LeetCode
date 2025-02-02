#URL: https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while fast != 1 and self.nextnum(fast) != 1:
            slow = self.nextnum(slow)
            print(f"slow {slow}")
            fast = self.nextnum(self.nextnum(fast))
            print(f"fast {fast}")
            if slow == fast:
                return False
        return True
    
    def nextnum(self, num):
        print(f"num: {num}")
        str_num = str(num)
        squared_sum =  0
        for i in str_num:
            int_dig = int(i)
            squared_sum += int_dig ** 2
            print(f"sqsum: {squared_sum}")
        return squared_sum 
