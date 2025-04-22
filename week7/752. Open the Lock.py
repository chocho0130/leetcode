from collections import deque # 引入 deque，讓我們可以高效地進行 BFS 的 queue 操作
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 把 deadends 轉成 set，加速查找速度（O(1)）
        dead = set(deadends)
        
        # 建立一個 set 來記錄已經拜訪過的狀態，避免重複走訪
        visited = set('0000')
        
        # 如果一開始就是死結，那就無法開始
        if '0000' in dead:
            return -1
        
        # 使用 queue 進行 BFS，每個元素是 (目前狀態, 已經走的步數)
        queue = deque([('0000', 0)])

        while queue:
            # 取出目前的狀態和步數
            code, steps = queue.popleft()
            
            # 如果已經是目標狀態，直接回傳步數
            if code == target:
                return steps
            
            # 嘗試旋轉每一位數字
            for i in range(4):
                digit = int(code[i])  # 取得目前這一位的數字
                
                # 每一位數字可以往前或往後轉（-1 或 +1）
                for move in [-1, 1]:
                    # 新的數字是原來的數字加上 move，並用 %10 處理環狀轉動
                    new_digit = (digit + move) % 10
                    
                    # 把新的數字放回原來的位置，形成新的 lock 狀態
                    new_code = code[:i] + str(new_digit) + code[i+1:]
                    
                    # 如果這個狀態不是死結，也還沒拜訪過，就加入 queue
                    if new_code not in dead and new_code not in visited:
                        visited.add(new_code)            # 標記為已拜訪
                        queue.append((new_code, steps + 1))  # 加入 queue，步數 +1
        
        # 如果整個 BFS 都找不到目標狀態，表示無法解開鎖
        return -1