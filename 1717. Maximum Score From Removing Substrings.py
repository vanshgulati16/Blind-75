# Question: https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2024-07-12

# Approach: the approach is very simple(Greedy approach) we will first check if x>y or vice versa if x is greater we know that by removing 'ab' we will get max point so we will maintain a stack and keep
# adding element and when ever we hit 'ab' we add x points to res, we are absolutely certain that we won't inculcate any 'ab' in stack once we iterate through it. now we create one more stack
# to find 'ba' in the previous stack if any, if we incur 'ba' we increment the res by y. hence after the whole iteration we will have the maximum score.

# TC: O(N), since we go through string twice.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0

        if x>y:
            high = "ab"
            high_score = x
            low = "ba"
            low_score = y
        else:
            high = "ba"
            high_score = y
            low = "ab"
            low_score = x
        
        stack = []
        for char in s:
            if char == high[1] and stack and stack[-1] == high[0]:
                res += high_score
                stack.pop()
            else:
                stack.append(char)

        new_stack = []
        for char in stack:
            if char == low[1] and new_stack and new_stack[-1] == low[0]:
                res += low_score
                new_stack.pop()
            else:
                new_stack.append(char)
        return res

