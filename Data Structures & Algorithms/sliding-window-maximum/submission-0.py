from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()

        result = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < r - k + 1:
                q.popleft()

            if r >= k - 1:
                result.append(nums[q[0]])

        return result