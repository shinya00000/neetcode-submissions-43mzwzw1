class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        minnums= min(nums)
        hash_list=[None]*(max(nums)-minnums + 1)
        for i in range(0,len(nums)):
            if nums[i]==hash_list[nums[i]-minnums]:
                return True
            else:
                hash_list[nums[i]-minnums] = nums[i]
        return False
