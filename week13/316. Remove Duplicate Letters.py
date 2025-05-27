class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}  # 每個字母最後出現位置
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue  # 已經放進 stack 的就跳過

            # 移除比當前字母大、後面還會再出現的字母（才能保證字典序更小）
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)
