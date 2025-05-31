from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_do(k: int) -> bool:
            # 判斷是否能完成 k 個任務
            # 取出最難的 k 個任務（tasks尾部）
            # 取出最強的 k 個工人（workers尾部）
            # 使用雙端佇列存放可用工人強度，試著用藥水分配
            dq = deque()
            p = pills
            i = len(workers) - 1
            for task in reversed(tasks[:k]):
                # 把可用強度 >= task - strength的工人放入dq，因為他們用藥水可以勝任該任務
                while i >= len(workers) - k and i >= 0 and workers[i] + strength >= task:
                    dq.appendleft(workers[i])
                    i -= 1

                if dq:
                    # 優先用強度 >= task 的工人完成任務，不用藥水
                    if dq[-1] >= task:
                        dq.pop()
                    else:
                        # 強度不足但可用藥水補強
                        if p == 0:
                            return False
                        p -= 1
                        dq.popleft()  # 使用最弱工人，藥水補足
                else:
                    # 沒有工人可用，任務無法完成
                    return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_do(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
