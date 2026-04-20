class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == None:
            return 0
        left = 0
        max_length = 0
        count = dict()
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_f = max(count.values())
            if (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length