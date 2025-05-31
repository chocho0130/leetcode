from typing import List
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0 or indexDiff <= 0:
            return False

        window = SortedList()
        for i in range(len(nums)):
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])

            pos = window.bisect_left(nums[i] - valueDiff)
            if pos < len(window) and abs(window[pos] - nums[i]) <= valueDiff:
                return True

            window.add(nums[i])

        return False
