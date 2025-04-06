from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []  # 用來存放所有合法解（每一個解是一個棋盤）

        # 建立一個 n x n 棋盤，預設都是 '.'（代表空格）
        board = [['.' for _ in range(n)] for _ in range(n)]

        # 建立 3 個集合來記錄哪些欄位、對角線上已經有皇后
        cols = set()       # 記錄已經被佔用的「欄」（column）
        diag1 = set()      # 記錄主對角線（\），用 row - col 代表
        diag2 = set()      # 記錄副對角線（/），用 row + col 代表

        # 定義一個回溯函式：目前在第 row 行要放皇后
        def backtrack(row):
            # 如果 row == n，表示 n 行都放完了，這是一組合法解
            if row == n:
                # 把棋盤的每一列轉成字串，再整體加入答案
                solution = [''.join(r) for r in board]
                result.append(solution)
                return

            # 遍歷這一行的每一個欄位，看哪裡可以放皇后
            for col in range(n):
                # 檢查目前欄位或對角線是否已經有皇后
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # 有衝突，跳過這個位置

                # 做選擇：在 (row, col) 放一個皇后
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                #  遞迴處理下一行
                backtrack(row + 1)

                #  撤銷選擇（Backtrack）：移除皇后，還原狀態
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # 從第 0 行開始放皇后
        backtrack(0)

        return result