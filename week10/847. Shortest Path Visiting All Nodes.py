from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque()
        visited = set()

        # 初始：從每個節點出發，visited 狀態只有自己
        for i in range(n):
            mask = 1 << i  # bitmask 表示目前走過的節點
            queue.append((i, mask, 0))  # (目前節點, 訪問狀態, 步數)
            visited.add((i, mask))

        final_state = (1 << n) - 1  # 例如 n=3，則 final_state = 0b111

        while queue:
            node, mask, steps = queue.popleft()
            if mask == final_state:
                return steps  # 走完所有節點

            for nei in graph[node]:
                next_mask = mask | (1 << nei)
                if (nei, next_mask) not in visited:
                    visited.add((nei, next_mask))
                    queue.append((nei, next_mask, steps + 1))

        return -1  # 理論上不會發生
