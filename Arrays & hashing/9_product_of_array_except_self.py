class Solution:
    # brute force O(n^2)
    def productExceptSelf1(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            for j, n in enumerate(nums):
                if i == j:
                    continue
                res[i] *= n
        
        return res
    # optimal O(n) (prefix and suffix)
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
    # division O(n)
    def productExceptSelf3(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        product = 1
        zeroCount = 0
        
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
        
        if zeroCount > 1:
            return res
        
        for i in range(len(nums)):
            if zeroCount == 1:
                if nums[i] == 0:
                    res[i] = product
            else:
                res[i] = product // nums[i]
        
        return res
                
        