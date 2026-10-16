class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        for i in range(l, r):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = l + r // 2
            elif nums[i] > target:
                return -1

        return -1