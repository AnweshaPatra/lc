class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        pos, neg = 0, 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            elif nums[i] < 0:
                ans[neg] = nums[i]
                neg += 2
        return ans