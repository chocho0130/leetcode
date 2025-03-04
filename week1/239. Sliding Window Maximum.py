from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        
        deq = deque()  # 存放索引，維持一個遞減序列，deq[0] 永遠是當前窗口最大值的索引
        output = []
        
        for i in range(len(nums)):
            # 檢查隊首是否超出當前窗口範圍
            if deq and deq[0] == i - k:
                deq.popleft()
            
            # 當前元素大於隊尾的元素時，不斷彈出隊尾，因為它們永遠無法成為窗口最大值
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            deq.append(i)
            
            # 當窗口形成後（i >= k-1），將當前窗口最大值加入結果
            if i >= k - 1:
                output.append(nums[deq[0]])
        
        return output
