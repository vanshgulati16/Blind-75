# Question: https://leetcode.com/problems/pass-the-pillow/description/?envType=daily-question&envId=2024-07-06 

# Approach: at t=1 pass will be at n = 2, t=2 pass will be at n = 3, therefore at t = n-1 pass will be at n, hence we conclude that hops will be equal to time that is there will be n-1 hops
# for n elements. Hence flips will be total time divided by number of hops(time//(n-1)), Now that we have flip we can check if it is odd or even and if it is even we know that the pass is at
# 0th position which is element 1 so we check if there is any remainder(time%(n-1)) we add it to the 0th position to get the actual position and vise versa for odd flips.

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        flips = time//(n-1)

        if time < n :
            return time+1
        else:
            if flips%2 == 0:
                return 1 + time%(n-1)
            else:
                return n - time%(n-1)
