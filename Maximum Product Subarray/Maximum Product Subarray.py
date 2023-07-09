class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # create two arrays max and min and initialize it by inital elelement of nums array
        max_product = [nums[0]]*n
        min_product = [nums[0]]*n
        print(f"Initial max product {max_product}")
        print(f"Initial min product {min_product}")
        # iterate over the array from index 1 to n
        for i in range(1, n):
            # update the max product ith index with max of three values i.e 
            # nums element on ith index , product of i-1th index element of max_product with nums ith index and product of i-1th index element of min_product with nums ith index
            max_product[i] = max(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])
            print(f"max_product at {i} = {max_product[i]}")
            #  repate the same step but instead of max use min to update the min product i th index
            min_product[i] = min(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])
            print(f"min_product at {i} = {min_product[i]}")
            print(f"updated max_product = {max_product}")
            print(f"updated min_product = {min_product}")
        # return the max of the max_product
        return max(max_product)

  # Time complexity: O(N)
  # Space complexity: O(N) 
