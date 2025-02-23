#URL: https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == i+1:
                i += 1
            else:
                j = nums[i]
                if nums[j-1] == j:
                    return nums[i]
                else:
                    nums[j-1], nums[i] = nums[i], nums[j-1]
