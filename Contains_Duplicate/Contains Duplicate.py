class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap with key(nums[i])-> value(i)
        map_num = {}
        # iterate over the nums array
        for i in range(len(nums)):
            # check if the same element is in the hashmap
            if nums[i] in map_num:
                return True
            # if not then push the value
            else:
                map_num[nums[i]] = i
        return False
