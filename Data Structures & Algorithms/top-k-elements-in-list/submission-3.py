class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sor_keys = sorted(c.keys(),key= lambda x: c[x],reverse=True)
        return sor_keys[:k]