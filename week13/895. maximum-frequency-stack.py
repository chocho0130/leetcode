from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)          # 紀錄 val 出現的頻率
        self.group = defaultdict(list)        # 每個頻率對應一個 list
        self.max_freq = 0                     # 當前最大頻率

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        if f > self.max_freq:
            self.max_freq = f

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:  # 如果這一層頻率空了
            self.max_freq -= 1
        return val