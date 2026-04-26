class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            # 各繰り返しはres[i]を求めるのが目的
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                # これより先にres[j]より大きい要素がないのでbreak
                if res[j] == 0:
                    j = n
                    break
                # temperatures[j]より大きい要素はtemperatures[j+res[j]]以降にしかないのでジャンプ
                j += res[j]

            if j < n:
                res[i] = j - i
        return res