class Solution:
    def longestConsecutive1(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
      
    def longestConsecutive2(self, nums: list[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak = 0
            curr = num

            while curr in store:
                curr += 1
                streak += 1
            
            res = max(res, streak)
            
        return res
    
    
    def longestConsecutive3(self, nums: list[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
    

            
        