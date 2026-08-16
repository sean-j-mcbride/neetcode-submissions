class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countd = defaultdict(int)

        for num in nums:
            if num not in countd.keys():
                countd[num] = 1
            else:
                countd[num] += 1
        
        countl = []
        for key, val in countd.items():
            countl.append((key, val))
        countl.sort(key = lambda x: x[1], reverse = True)
        out = []
        for i in range(k):
            out.append(countl[i][0])
        
        return out
