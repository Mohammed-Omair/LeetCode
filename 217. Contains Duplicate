#URL https://leetcode.com/problems/contains-duplicate/
#1st solution that came into my mind TC: O(nlogn) SC: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return False
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
#2nd Solution after watching the video TC: O(n) SC: 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
