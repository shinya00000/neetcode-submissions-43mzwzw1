class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # t の文字の必要数をカウント
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have: 条件を満たした文字の種類数
        # need: 必要な文字の種類数（t のユニークな文字数）
        have, need = 0, len(countT)
        
        # 答えを記録する変数 (最小の長さ, 左端と右端のインデックス)
        res, resLen = [-1, -1], float("infinity")
        
        countS = {} # 現在のウィンドウ内の文字をカウントする辞書
        l = 0

        # 右ポインタ r を進めてウィンドウを広げる
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)

            # 追加した文字が t に含まれており、かつ必要な個数に達したら have を増やす
            if c in countT and countS[c] == countT[c]:
                have += 1

            # 必要な文字がすべて揃っている間、左ポインタ l を進めてウィンドウを縮める
            while have == need:
                # 最小の長さを更新する
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # 左端の文字をウィンドウから外す
                left_char = s[l]
                countS[left_char] -= 1
                
                # 外したことで条件を満たさなくなったら have を減らす
                if left_char in countT and countS[left_char] < countT[left_char]:
                    have -= 1
                
                # 左ポインタを右へ進める
                l += 1

        # 最終的な答えの文字列を返す
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            
