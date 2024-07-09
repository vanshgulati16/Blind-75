# Question: https://leetcode.com/problems/average-waiting-time/description/?envType=daily-question&envId=2024-07-09

# Approach: As we know that a chef can only cater one individual at a time so we will save the chef time in a variable and we will
# loop around the customer to and check if the chef is available or when he is going to be available next we will add the time 
# on the average waiting time with the meal peperation time and we will deduct the arrival time to get the wait time for each 
# customer adn hence divide the total wait time of all the customer by number of customer to get the average wait time.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avg_wt = 0
        c_t = 0

        for i in range(len(customers)):
            if c_t < customers[i][0]:
                avg_wt = avg_wt + customers[i][1]
                c_t = customers[i][0]+ customers[i][1]

            else:
                avg_wt = avg_wt + (c_t + customers[i][1] - customers[i][0])
                c_t = c_t + customers[i][1]

        return avg_wt/len(customers)
