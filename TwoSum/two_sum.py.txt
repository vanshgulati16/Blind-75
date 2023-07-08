class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # created a hashmap to store number(key) -> index(value)
        h_map = {} 

        # looping over the array
        for i in range(len(nums)):
            # subract current number from the target and store it in a variable as complement
            complement = target - nums[i]
            # checking if the complement exist in hashmap
            if complement in h_map:
                # returning the indexes of complement and the number as they added up to the target
                return [h_map[complement], i]
            # else we are adding the current number to hashmap as number as key -> index(value)
            h_map[nums[i]] = i
        return []  # no solution found

        # Time compexity: O(n)