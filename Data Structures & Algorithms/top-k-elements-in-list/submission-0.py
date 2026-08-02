class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        sorted_elements = sorted(counts.keys(), key=counts.get, reverse=True)
        return sorted_elements[:k]