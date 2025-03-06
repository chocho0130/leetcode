class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # 當前窗口邊界，下一步能到達的最遠距離，跳躍次數
        current_end = 0
        current_farthest = 0
        jumps = 0
        
        for i in range(n - 1):
            current_farthest = max(current_farthest, i + nums[i])
            # 當走到當前窗口邊界，就需要跳躍
            if i == current_end:
                jumps += 1
                current_end = current_farthest
        return jumps
