class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cntlist = [0]
        setnums = set()
        for i in nums:
            if i not in setnums:
                cnt = 0
                j = i
                while j in nums:
                    cnt += 1
                    setnums.add(j)
                    j += 1
                cntlist.append(cnt)

        res = max(cntlist)
        return res

