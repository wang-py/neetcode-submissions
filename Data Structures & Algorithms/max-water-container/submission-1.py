class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = []

        while i < j:
            # print(f"i is {i}, j is {j}")
            area.append((j - i) * min(heights[i], heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1

        
        return max(area)