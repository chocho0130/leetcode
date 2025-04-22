class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        # 建立圖的鄰接表
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # 初始化
        res = [0] * n         # 存每個節點的距離總和
        count = [1] * n       # 子樹節點數量（包含自己），初始化為 1，因為自己也算一個
        visited = set()       # 記錄訪問過的節點

        # 第一次 DFS：計算 res[0] 和每個節點的 count 值
        def dfs(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    count[node] += count[neighbor]                   # 子樹節點數加總
                    res[node] += res[neighbor] + count[neighbor]    # 累加子樹的距離總和

        # 第二次 DFS：根據父節點的 res 計算子節點的 res
        def dfs2(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    # 利用公式從父節點計算子節點的距離總和
                    res[neighbor] = res[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)

        # 先從 0 開始計算
        dfs(0, -1)
        dfs2(0, -1)

        return res