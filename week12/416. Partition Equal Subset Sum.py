from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2

        # 初始化 DP 陣列
        # dp[i] 表示是否可以從 nums 中選擇一些數字，使其總和為 i
        dp = [False] * (target_sum + 1)

        dp[0] = True

        for num in nums:
            for i in range(target_sum, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[target_sum]
