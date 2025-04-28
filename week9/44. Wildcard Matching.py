from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s 的長度
        m = len(s)
        # p 的長度
        n = len(p)
        
        # 建立一個 (m+1) x (n+1) 的 DP 表，初始都是 False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 空字串對空模式，一定可以匹配
        dp[0][0] = True
        
        # 預處理：如果 p 前面是星號 *，可以匹配空字串
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        # 開始填 DP 表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果 p[j-1] 是普通字元 或 ?
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    # 看前一個字元是否匹配
                    dp[i][j] = dp[i-1][j-1]
                # 如果 p[j-1] 是 *
                elif p[j-1] == '*':
                    # * 可以當空字串（dp[i][j-1]）或吃掉一個字元（dp[i-1][j]）
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        
        # 回傳整個字串跟模式是否完全匹配
        return dp[m][n]