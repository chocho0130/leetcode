from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n  # 每個人至少一顆糖

        # 左到右遍歷，確保右邊的比左邊大時，糖果數量要比左邊多
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # 右到左遍歷，確保左邊的比右邊大時，糖果數量要比右邊多
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)  # 總糖果數量
