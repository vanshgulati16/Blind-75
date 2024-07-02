# Question: https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

# Approach: we will use the sliding window approach, one pointer in the begining and second in the end of the array, we will sort the 
# array and loop over it and check for sum of pair values equal to target, if yes count inc by 1 else we will check if sum of pair value 
# is less than k then inc left by 1 else dec right by 1.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0 #left pointer
        j = len(nums)-1 #right pointer
        nums.sort()

        while i<j :
            if nums[i] + nums[j] == k:
                count += 1
                i+= 1
                j -=1
            elif nums[i] + nums[j] < k:
                i+=1
            elif nums[i] + nums[j] > k:
                j -=1

        return count 
