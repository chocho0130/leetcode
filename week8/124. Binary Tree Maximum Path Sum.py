# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 使用一個 class 層級變數來記錄目前遇到的最大路徑和
        self.max_sum = float('-inf')  # 初始化為負無限，因為樹中節點可能為負數

        # 定義一個遞迴函數：回傳從當前節點「往下走」能得到的最大貢獻值
        def max_gain(node):
            if not node:
                return 0  # 空節點貢獻值為 0

            # 分別計算左右子樹的最大貢獻值
            # 如果貢獻值小於 0，代表那邊不值得加進來，所以取 max(0, 貢獻值)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 「以當前節點為最高點」的完整路徑價值（可以包含左右子樹）
            price_new_path = node.val + left_gain + right_gain

            # 嘗試更新全域最大路徑和
            self.max_sum = max(self.max_sum, price_new_path)

            # 回傳當前節點「能貢獻給上一層」的最大路徑值（只能選擇左或右，不能兩邊）
            return node.val + max(left_gain, right_gain)

        # 從 root 開始遞迴
        max_gain(root)

        # 回傳答案
        return self.max_sum
        