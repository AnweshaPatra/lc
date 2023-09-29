class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i + 1
            k = n - 1
            while k > j:
                sm = nums[i] + nums[j] + nums[k]
                if sm < 0:
                    j += 1
                elif sm == 0:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while k > j and nums[j] == nums[j - 1]: j += 1
                    while k > j and nums[k] == nums[k + 1]: k -= 1
                else:
                    k -= 1
        return ans