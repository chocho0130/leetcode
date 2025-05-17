from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        計算給定高度圖可以捕捉到的雨水總量。

        Args:
            height: 表示柱子高度的非負整數列表。

        Returns:
            可以捕捉到的雨水總量。
        """
        if not height:
            return 0 # 如果高度列表為空，無法捕捉雨水，返回 0

        left = 0  # 左指標，從列表開頭開始
        right = len(height) - 1  # 右指標，從列表結尾開始
        left_max = 0  # 記錄左邊遇到的最高柱子高度
        right_max = 0 # 記錄右邊遇到的最高柱子高度
        total_water = 0 # 累積捕捉到的雨水總量

        # 當左指標在右指標的左邊時，繼續迴圈
        while left < right:
            # 比較左右兩個指標當前的柱子高度
            if height[left] < height[right]:
                # 如果左邊的柱子比較矮，那麼左指標當前位置的積水高度
                # 取決於 left_max (因為右邊有更高的柱子擋著)
                if height[left] >= left_max:
                    # 如果當前左邊柱子比 left_max 高，更新 left_max
                    left_max = height[left]
                else:
                    # 否則，當前位置可以積水，積水量為 left_max 減去當前柱子高度
                    total_water += left_max - height[left]
                # 移動左指標向右
                left += 1
            else:
                # 如果右邊的柱子比較矮或相等，那麼右指標當前位置的積水高度
                # 取決於 right_max (因為左邊有更高的或相等的柱子擋著)
                if height[right] >= right_max:
                    # 如果當前右邊柱子比 right_max 高，更新 right_max
                    right_max = height[right]
                else:
                    # 否則，當前位置可以積水，積水量為 right_max 減去當前柱子高度
                    total_water += right_max - height[right]
                # 移動右指標向左
                right -= 1

        # 當 left >= right 時，指標相遇或交錯，迴圈結束
        # total_water 儲存了總的積水量
        return total_water
