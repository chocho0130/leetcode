from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 如果 intervals 是空的，直接回傳 0
        if not intervals:
            return 0
        
        # 依照每個區間的「結束時間」來排序，結束早的排前面
        intervals.sort(key=lambda x: x[1])
        
        # 初始化：保留第一個區間，記住它的結束時間
        end = intervals[0][1]
        
        # 要刪除的區間數，開始是 0
        remove_count = 0
        
        # 從第 2 個區間開始檢查
        for i in range(1, len(intervals)):
            # 如果現在這個區間的開始時間，比上個結束時間還早（有重疊）
            if intervals[i][0] < end:
                # 有重疊，要刪掉，所以刪除數量加 1
                remove_count += 1
            else:
                # 沒重疊，就更新 end，表示保留這個區間
                end = intervals[i][1]
        
        # 回傳總共要刪掉的區間數
        return remove_count