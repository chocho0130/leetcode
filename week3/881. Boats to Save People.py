from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # 先排序
        left, right = 0, len(people) - 1
        count = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # 輕的人也上船
            right -= 1  # 重的人一定要上船
            count += 1  # 計算這艘船

        return count
