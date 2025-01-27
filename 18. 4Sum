# URL: https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate i
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate j
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    quad_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if quad_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:  # Skip duplicate l
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:  # Skip duplicate r
                            r -= 1
                    elif quad_sum < target:
                        l += 1
                    else:
                        r -= 1
        return quadruplets
