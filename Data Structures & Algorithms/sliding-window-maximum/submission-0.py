class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums[0:k]:
            count[num] = count.get(num, 0) + 1
        res.append(max(count))
        nums_len = len(nums)
        for i in range(1,nums_len - k + 1):
            count[nums[i-1]] = count.get(nums[i-1],0) - 1
            if count.get(nums[i-1],0) == 0:
                del count[nums[i-1]]
            count[nums[i+k-1]] = count.get(nums[i+k-1],0) + 1
            res.append(max(count))
        return res