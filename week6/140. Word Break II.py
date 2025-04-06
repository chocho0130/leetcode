from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # 把字典轉成 set，查找更快速
        n = len(s)
        memo = {}  # 用來手動實作記憶化，key 是起始 index，value 是所有句子列表

        def dfs(start: int) -> List[str]:
            # 如果已經計算過從 start 開始的結果，就直接回傳（避免重算）
            if start in memo:
                return memo[start]

            if start == n:
                return [""]  # 已經處理到字串末尾，回傳空字串代表成功分割完畢

            sentences = []

            # 遍歷從 start 開始的所有可能切割位置
            for end in range(start + 1, n + 1):
                word = s[start:end]  # 取出當前要判斷的子字串

                if word in word_set:  # 如果是字典中的單字
                    # 遞迴處理剩下的部分
                    following_sentences = dfs(end)

                    for sentence in following_sentences:
                        if sentence == "":
                            sentences.append(word)  # 沒有剩下的部分，不加空格
                        else:
                            sentences.append(word + " " + sentence)  # 有剩下，空格拼接

            # 將當前結果儲存到 memo 中
            memo[start] = sentences
            return sentences

        return dfs(0)