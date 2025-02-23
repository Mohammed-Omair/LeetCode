#URL: https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        print(nums)
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == i+1 or nums[i] < 1 or nums[i] > n:
                i += 1
            else:
                j = nums[i]
                if nums[j-1] == j:
                    i += 1
                else:
                    nums[j-1], nums[i] = nums[i], nums[j-1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i+1
        return len(nums) + 1
            
