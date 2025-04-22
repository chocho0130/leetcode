# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 主函數，接收一個樹的根節點 root，兩個目標節點 p 和 q
        # base case：若當前節點為空（代表遍歷到底了），或 root 就是 p 或 q，則直接返回 root
        # 因為 root 就是我們要找的其中一個節點，或是 subtree 找到底都沒東西
        if not root or root == p or root == q:
            return root

        # 在左子樹中遞迴尋找 p 或 q 的蹤跡
        left = self.lowestCommonAncestor(root.left, p, q)

        # 在右子樹中遞迴尋找 p 或 q 的蹤跡
        right = self.lowestCommonAncestor(root.right, p, q)

        # 若左子樹與右子樹都有找到非空結果，表示 p 和 q 分別在左右兩邊
        # 那麼此時的 root 就是最小公共祖先（lowest common ancestor）
        if left and right:
            return root

        # 若只有一邊找到（另一邊是 None），就往上回傳找到的那一邊
        # 若兩邊都是 None，也會回傳 None，代表此路線找不到
        return left if left else right
        