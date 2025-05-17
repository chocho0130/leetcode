class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        計算確定雞蛋臨界樓層所需的最小扔蛋次數。

        Args:
            k: 雞蛋數量。
            n: 樓層數量。

        Returns:
            所需的最小扔蛋次數。
        """
        # dp[j] 表示在當前扔蛋次數下，使用 j 個雞蛋最多可以確定的樓層數
        dp = [0] * (k + 1)

        # moves 表示當前的扔蛋次數
        moves = 0

        # 當前扔蛋次數下，用 k 個雞蛋能確定的樓層數還不足 n 層時，增加扔蛋次數
        # dp[k] 儲存了當前 moves 次扔蛋、k 個雞蛋能測的最大樓層數
        while dp[k] < n:
            moves += 1
            # 更新 dp 陣列。從 k 向 1 遍歷是為了使用上一輪 (moves-1 次) 的 dp[j-1] 和 dp[j]
            for j in range(k, 0, -1):
                # 根據狀態轉移方程：
                # dp[j] (用 moves 次扔 j 個蛋) =
                # dp[j-1] (moves-1 次扔 j-1 個蛋，雞蛋破了，在下面能測的層數) +
                # dp[j] (moves-1 次扔 j 個蛋，雞蛋沒破，在上面能測的層數) +
                # 1 (當前扔的這一層)
                dp[j] = dp[j - 1] + dp[j] + 1

        # 當迴圈結束時，moves 就是第一次使得 dp[k] >= n 的扔蛋次數
        return moves
