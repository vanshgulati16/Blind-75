# Question: https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22

# Approach: 

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        hash_map = {}
        for i in range(len(heights)):
            hash_map[heights[i]] = names[i]
        
        sorted_keys= list(hash_map.keys())
        sorted_keys.sort(reverse = True)

        for key in sorted_keys:
            res.append(hash_map[key])
        return res
