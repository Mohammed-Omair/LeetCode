class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0

        for i in range(len(nums)):
            if count == 0:
                result = nums[i]
            
            count += (1 if result == nums[i] else -1)
        
        return result
        