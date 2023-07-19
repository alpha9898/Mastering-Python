class Solution:
    def removeTrailingZeros(self, nums: str) -> str:
        i = len(nums) - 1
        while i >= 0 and nums[i] == '0':
            i -= 1
        return nums[:i + 1]