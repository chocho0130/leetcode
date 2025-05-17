import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # 最小的速度是 1 (每小時至少吃一根)
        low = 1
        # 最大的速度是所有香蕉堆中數量最多的那一堆 (最壞情況下，每小時吃完一堆)
        high = max(piles)

        # 開始二分搜尋
        while low <= high:
            # 猜測一個中間速度
            mid = (low + high) // 2
            # 計算在這個速度下吃完所有香蕉需要的時間
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / mid)  # 用 ceil 確保即使吃不完也要算一個小時

            # 如果所需時間小於等於總時間 h，表示這個速度可行，我們可以嘗試更小的速度
            if hours_needed <= h:
                high = mid - 1
            # 如果所需時間大於總時間 h，表示這個速度太慢了，我們需要更快的速度
            else:
                low = mid + 1

        # 當迴圈結束時，low 就是最小的可行速度
        return low