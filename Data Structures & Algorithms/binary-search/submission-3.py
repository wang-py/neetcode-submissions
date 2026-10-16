class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        n = r

        for i in range(l, r):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = l + n // 2
                n = n // 2
                continue
            elif nums[i] > target:
                return -1

        return -1