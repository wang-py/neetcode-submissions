class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n
        total_trapped = 0
        prefix_max[0] = height[0]
        suffix_max[n - 1] = height[n - 1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])
        
        for i in range(n):
            trapped = min(prefix_max[i], suffix_max[i]) - height[i]
            total_trapped += trapped
        
        return total_trapped