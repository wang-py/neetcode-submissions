class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            output[i] *= prefix
            # print(f"output is {output}")
        
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]
            # print(f"suffix output is {output}")
                
        return output