# Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02
# Approach: first find the larger array convert it into hash table(numbers => count) and then loop over the other array to find
# the intersecting element and append it into ans, after every intersting element reduce the map count 
# by 1(to handle the same length situtatiions)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        if len(nums1)<=len(nums2):
            nums_map = Counter(nums2)
            for i in nums1:
                if i in nums_map.keys() and nums_map[i] != 0:
                    nums_map[i] -= 1
                    ans.append(i)
        else:
            nums_map = Counter(nums1)
            for i in nums2:
                if i in nums_map.keys() and nums_map[i] != 0:
                    nums_map[i] -= 1
                    ans.append(i)
        return ans
