class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        # recursive binary tree
        if l > r:
            return -1
        i = l + (r - l) // 2
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return self.binary_search(l, i-1, nums, target)
        elif nums[i] < target:
            return self.binary_search(i+1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
         return self.binary_search(0, len(nums) - 1, nums, target)