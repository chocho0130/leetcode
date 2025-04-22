from typing import List  # 引入 List 類型提示功能

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 建立一個 dp 陣列，長度為 amount+1，初始值都設成無限大（表示一開始無法湊到）
        dp = [float('inf')] * (amount + 1)
        
        # 基本情況：金額 0 不需要任何硬幣，因此設成 0
        dp[0] = 0

        # 對每一種硬幣進行遍歷（外層迴圈是所有硬幣面額）
        for coin in coins:
            # 對於從該硬幣面額開始，到目標金額為止的所有金額進行更新
            for x in range(coin, amount + 1):
                # 狀態轉移公式：
                # 若要湊出金額 x，則可以考慮用「湊出 x - coin 的最小硬幣數 + 1 枚 coin」
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # 最後回傳 dp[amount]，如果還是無限大，代表無法湊出這個金額
        return dp[amount] if dp[amount] != float('inf') else -1