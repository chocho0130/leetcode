from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        計算戳破氣球能獲得的最大金幣數量。

        Args:
            nums: 氣球上數字的列表。

        Returns:
            能獲得的最大金幣數量。
        """
        # 在 nums 的頭尾添加虛擬氣球 1，方便處理邊界情況
        new_nums = [1] + nums + [1]
        n = len(new_nums)

        # dp[i][j] 表示戳破 new_nums 中索引範圍在 (i, j) 之間
        # (不包括 i 和 j) 的所有氣球所能獲得的最多金幣
        # 陣列大小為 n x n
        dp = [[0] * n for _ in range(n)]

        # 遍歷區間長度 (從 2 開始，因為區間至少需要包含一個氣球，
        # 在 new_nums 中，一個氣球位於兩個虛擬氣球之間，長度至少為 2)
        for length in range(2, n):
            # 遍歷區間的起始索引 i
            # i 的範圍是 [0, n - length - 1]，確保 j 不越界
            for i in range(n - length):
                # 區間的結束索引 j
                j = i + length

                # 在區間 (i, j) 中，遍歷所有可能的最後被戳破的氣球 k
                # k 的範圍是 (i, j)，即 i+1 到 j-1
                for k in range(i + 1, j):
                    # 如果 k 是最後被戳破的氣球：
                    # 1. 戳破 k 獲得的金幣：new_nums[i] * new_nums[k] * new_nums[j]
                    #    此時 new_nums[i] 和 new_nums[j] 是 k 的鄰居
                    # 2. 戳破 (i, k) 區間內的氣球獲得的最大金幣：dp[i][k]
                    # 3. 戳破 (k, j) 區間內的氣球獲得的最大金幣：dp[k][j]
                    coins = dp[i][k] + dp[k][j] + new_nums[i] * new_nums[k] * new_nums[j]

                    # 更新 dp[i][j] 的最大值
                    dp[i][j] = max(dp[i][j], coins)

        # 最終結果是戳破原始陣列所有氣球的最大金幣，對應 new_nums 的 (0, n-1) 區間
        # 也就是 dp[0][n - 1]
        return dp[0][n - 1]

# # 範例使用：
# sol = Solution()
# nums1 = [3, 1, 5, 8]
# print(f"氣球: {nums1}, 最大金幣: {sol.maxCoins(nums1)}") # 預期輸出: 167
# # 解釋：[3,1,5,8] -> [3,5,8] (3*1*5=15) -> [3,8] (3*5*8=120) -> [8] (1*3*8=24) -> [] (1*8*1=8)
# # 總計: 15 + 120 + 24 + 8 = 167

# nums2 = [1, 5]
# print(f"氣球: {nums2}, 最大金幣: {sol.maxCoins(nums2)}") # 預期輸出: 10
# # 解釋：[1,5] -> [5] (1*1*5=5) -> [] (1*5*1=5)
# # 總計: 5 + 5 = 10