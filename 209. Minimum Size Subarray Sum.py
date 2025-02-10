#URL: https://leetcode.com/problems/minimum-size-subarray-sum/
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        window_end = 0
        windows_sum = 0
        min_length = math.inf
        for window_end in range (len(nums)):
            windows_sum += nums[window_end]
            while windows_sum >= target:
                min_length = min(window_end - window_start + 1, min_length)
                windows_sum -= nums[window_start]
                window_start += 1
        # TODO: Write your code here
        return min_length if min_length != math.inf else 0