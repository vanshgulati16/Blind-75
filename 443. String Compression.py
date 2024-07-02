# Question: https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

# Approach(Copied From Leetcode Solution):
# Here we are using two pointers, one for iterating through the original character array and one for keeping track of the current position in the compressed array. The two pointer variables used are i and ans.
# Now also use a variable to keep track of the count of consecutive characters.
# First set the current letter to the first character in the array and initializes the count to 0.
# Then iterate through the array until you find a different character or reach the end of the array.
# For each iteration, increment the count and the index i.
# When you find a different character or reach the end of the array, write the current letter to the compressed array and, if the count is greater than 1, write the count as a string to the compressed array.
# Then reset the count to 0 and set the current letter to the new letter.

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 # this is for checking for same element.
        ans = 0  #this is to iterate over chars for in place changes.

        while i< len(chars):
            letter = chars[i]
            count = 0
            while i< len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1   
            if count >1:
                for c in str(count):
                    chars[ans] = c
                    ans +=1
        return ans
