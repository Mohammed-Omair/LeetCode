#URL: https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicateNumbers = []
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == i+1:
                i += 1
            else:
                j = nums[i]
                if nums[j-1] == j:
                    i += 1
                else:
                    nums[j-1], nums[i] = nums[i], nums[j-1]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicateNumbers.append(nums[i])
        return duplicateNumbers
