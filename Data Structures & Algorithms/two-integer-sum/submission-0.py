class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            
            seen[num] = idx
        