class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res_i = 1
            for j in range(i):
                res_i *= nums[j]
            for j in range(i+1,len(nums)):
                res_i *= nums[j]
            res.append(res_i)
        return res