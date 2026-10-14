class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        output = []
        n = len(nums_sorted)
        for i in range(n - 2):
            if nums_sorted[i] > 0:
                break
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            start = i + 1
            end = n - 1
            while start < end:
                total = nums_sorted[i] + nums_sorted[start] + nums_sorted[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    output.append([nums_sorted[i], nums_sorted[start], nums_sorted[end]])
                    start += 1
                    end -= 1
                    while start < end and nums_sorted[start] == nums_sorted[start - 1]:
                        start += 1
        
        return output