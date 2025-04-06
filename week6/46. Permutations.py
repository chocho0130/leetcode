from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # 用來存最後所有的排列結果，例如 [[1,2,3], [1,3,2], ...]

        # 回溯函式：path 是目前走到的排列結果，remaining 是還沒用過的數字
        def backtrack(path, remaining):
            # 當剩下的數字用完了，表示目前 path 是一組完整排列
            if not remaining:
                result.append(path[:])  # 將 path 的複製加入結果中（要複製，避免引用變動）
                return
            
            # 遍歷目前剩下的每一個數字
            for i in range(len(remaining)):
                # 1. 選擇一個數字，把它加到 path 裡
                path.append(remaining[i])

                # 2. 遞迴呼叫，處理剩下的數字（移除目前選的那一個）
                # 例如：remaining=[1,2,3], i=1，則新的 remaining 是 [1,3]（不包含 2）
                backtrack(path, remaining[:i] + remaining[i+1:])

                # 3. 撤銷選擇，把剛剛加入的數字移除（進行回溯）
                path.pop()

        # 從空排列開始，所有數字都還沒用過
        backtrack([], nums)

        return result