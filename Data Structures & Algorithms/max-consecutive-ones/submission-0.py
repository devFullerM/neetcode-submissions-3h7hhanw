class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                max_ones = max(max_ones, current)
            else:
                current = 0

        return max_ones
    
