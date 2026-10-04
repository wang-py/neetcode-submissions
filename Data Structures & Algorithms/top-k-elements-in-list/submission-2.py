class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        OFFSET = 1000
        counts = [0] * 2001
        for x in nums:
            counts[x + OFFSET] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for i, c in enumerate(counts):
            if c > 0:
                buckets[c].append(i - OFFSET)

        result = []
        for f in range(len(nums), 0, -1):
            for x in buckets[f]:
                result.append(x)
                if len(result) == k:
                    return result
        return result       
