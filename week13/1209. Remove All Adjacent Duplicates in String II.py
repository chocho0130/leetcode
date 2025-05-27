class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # 每個元素是 [字元, 次數]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # 次數達到 k，刪掉
            else:
                stack.append([char, 1])

        # 組合剩下的內容
        return ''.join(char * count for char, count in stack)