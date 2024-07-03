# Question: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03

# Approach: first we will sort the array in ascending order to make our life easier, then as we can do 3 updates atmost we 
# would return min difference of large and small element as 0 for arrays who's length is less then or equal to 3 or 4, but for
# the other cases, we will check by neglecting 3 elements from begining, ending, 2 from right and 1 from left, and 1 from right
# and 2 from left and hence finding the difference btw the largest and smallest element in each case and returning the least of them.

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        min_val = float('inf')

        if n <= 4:
            return 0
        else:
            # neglecting right 3 elements
            min_val = min(min_val, nums[n-4] - nums[0])
            # neglecting 3 left
            min_val = min(min_val, nums[n-1] - nums[3])
            # neglecting 2 left and 1 right
            min_val = min(min_val, nums[n-2] - nums[2])
            # neglecting 1 left and 2 right
            min_val = min(min_val, nums[n-3] - nums[1])
        return min_val
