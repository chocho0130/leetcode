class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return pow(x,n)
                

        # return x**n
        # 當 n 為負數時，轉換為正數冪次並取倒數
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0  # 初始化答案
        # 利用快速冪的思想：將 n 分解為二進位表示，每一位對應一次平方操作
        while n:
            # 如果 n 的當前最低位是1，則將當前 x 累乘到結果中
            if n % 2 == 1:
                result *= x
            # 平方 x，準備處理下一個二進位位元
            x *= x
            # 右移一位（整除2）
            n //= 2

        return result
