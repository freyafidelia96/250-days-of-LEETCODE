import math

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count, res = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

        # countNumbers = {}
        # x = math.floor(len(nums) / 2)

        # for i, n in enumerate(nums):
        #         if n in countNumbers:
        #             countNumbers[n] += 1
        #         else:
        #             countNumbers[n] = 1

        # for key, value in countNumbers.items():
        #      if value > x:
        #         return key
        
if __name__ == "__main__":
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
        