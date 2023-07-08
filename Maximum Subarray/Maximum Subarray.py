class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initiate a variable max sum with a value of initial array element
        max_sum = nums[0]
        # assign same value to current sum as we are starting from the begining 
        currentsum = nums[0]
        # iterate over the array and find max current value and check with the before max value if it is greater
        for num in nums[1:]:
            currentsum = max(num,currentsum + num)
            max_sum = max(max_sum, currentsum)
        # hence return the max value
        return max_sum

        # Time complexity: O(N)
        # Space Complexity: O(1)
        # Algo Used: Kadane's Algorithm
