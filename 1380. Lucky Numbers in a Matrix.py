# Question: https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=daily-question&envId=2024-07-19

# Approach: As we need to find the lucky number, i.e a number which is min value in a row and max value in a column, so to do that we will first find all the mininum values in all the rows and 
# store it in a set, then we will find all the max number in all the columns and store it in a set and then apply and operation to get the column elements in the set and return it in a list.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = {min(r) for r in matrix}
        max_col = {max(c) for c in zip(*matrix)} #Transpose of the matrix can be written as zip(*matrix)

        return list(min_row & max_col)
        
