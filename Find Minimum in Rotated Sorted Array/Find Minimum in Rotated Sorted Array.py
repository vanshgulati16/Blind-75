class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # initate low and high
        low = 0
        high = n-1
        # iterate until low < high
        while low<high:
            # initialize mid if array is rotated 
            mid = (low + high) //2
            print(f"mid = {mid}")
            print(f"mid value = {nums[mid]}")
            # check which way to traverse (if nums[mid] > nums[high] then minimum is on the right side else left side)
            if nums[mid]>nums[high]:
                low = mid + 1
            else:
                high = mid
        # return low as it will contains the minium element
        return nums[low]

  # Time Complexity: O(log n)
  #  Space complexity: O(1)
  # Alog used: Binary Search
  #  if using inbuild method of python directly use min(array)
