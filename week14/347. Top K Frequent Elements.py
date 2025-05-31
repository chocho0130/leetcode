from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        group = defaultdict(list)
        max_freq = 0
        for i in nums:
            freq[i] += 1
            f =freq[i]
            group[f].append(i)
            if f > max_freq:
                max_freq = f
        ans=[]
        ans_num=0
        while(ans_num!=k):
            val = group[max_freq].pop()
            freq[val] -= 1
            if not group[max_freq]:  # 如果這一層頻率空了
                max_freq -= 1
            if val not in ans:
                ans.append(val)
                ans_num+=1
        return ans

