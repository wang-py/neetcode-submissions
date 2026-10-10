class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = [0, 0]
        start = 0
        end = len(numbers) - 1
        while True:
            two_sum = numbers[start] + numbers[end]
            if two_sum < target:
                start += 1
                continue
            if two_sum > target:
                end -= 1
                continue
            else:
                output[0] = start + 1
                output[1] = end + 1
                break
        
        return output