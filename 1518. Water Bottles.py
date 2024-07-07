# Question: https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07

# Approach: we have two variables numBotteles and numExchange, to find the total water bottles we can drink after exchange will be, actual number of bottels that are present, now we will add
# number of exchange we can perform(numBottles//numExchange), but too keep in mind we have to change numBottels every time after exchange(numBottles//numExchange + numBottles%numExchange).

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        drink = numBottles

        if numBottles < numExchange:
            return drink
        
        while numBottles >= numExchange:
            temp = 0
            temp = numBottles//numExchange + numBottles%numExchange
            drink = drink + numBottles//numExchange
            numBottles = temp
        return drink
