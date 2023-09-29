class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = -1e9
        n = len(nums)
        prex = 1
        sufx = 1
        for i in range(n):
            if prex == 0: prex = 1
            if sufx == 0: sufx = 1
            prex *= nums[i]
            sufx *= nums[n-i-1]
            mx = max(mx, max(prex, sufx))
        return mx
