from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)  # 牆的總數
        
        # 初始化 DP 陣列：dp[i] = 還剩 i 面牆要刷時，最小花費
        # 因為最多有 n 面牆，所以陣列大小是 n+1
        # 一開始除了 dp[0]，其他都設成無限大 (代表不可能)
        dp = [float('inf')] * (n + 1)
        
        # 如果 0 面牆要刷，花費是 0
        dp[0] = 0
        
        # 遍歷每一面牆
        for i in range(n):
            # 這裡要反過來從大到小更新，避免重複使用同一面牆
            for j in range(n, -1, -1):
                # 下一步剩下的牆數
                next_wall = max(0, j - time[i] - 1)
                
                # 嘗試用這面牆，更新 dp[j]
                dp[j] = min(dp[j], dp[next_wall] + cost[i])
        
        # 最後答案是還有 n 面牆要刷時的最小花費
        return dp[n]