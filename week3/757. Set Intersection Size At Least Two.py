class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 1. 按照右端點升序排序，如果右端點相同，則按照左端點降序排序
        intervals.sort(key=lambda x: (x[1], -x[0]))
        print(intervals)
        # 初始化兩個數字，x 為較小的數，y 為較大的數
        x, y = -1, -1
        res = 0  # 記錄所選數字的總數
        
        # 2. 遍歷每個區間
        for a, b in intervals:
            # 如果 x 在區間 [a, b] 內，那麼 y 也一定在內（因為 x < y）
            if a <= x:
                continue  # 此區間已被覆蓋，不需額外新增數字
            # 如果只有 y 在區間內，則需要再選一個數字
            elif a <= y:
                res += 1
                # 選取 b 作為新的數字，更新 x 與 y
                x = y
                y = b
            else:
                # 如果 x 與 y 都不在區間內，需要新增兩個數字
                res += 2
                # 選擇 b-1 與 b 來覆蓋當前區間，並更新 x 與 y
                x = b - 1
                y = b
        return res