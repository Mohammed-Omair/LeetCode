#URL: https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            if nums[i] == i:
                i += 1
            elif nums[i] >= n:
                i += 1
            else:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n
        
