# Question: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2024-07-11

# Approach: So there is 2 approach, first approach is in O(N^2) which is commented out and the second approach is also known as the wormhole teleportation technique for this refer to
# this video(https://www.youtube.com/watch?v=65wVufni3tg), I'll go about approach 1, it is very simple as it is a paranthesis problem we will always go for stack to monitor the starting
# and closing paranthesis. We check if the string contains an open paranthesis if it does we add the index to the stack, else we append the char to the result(res), if we encounter a close
# paranthesis')', we pop stack to get it's starting paranthesis index and reverse the result from the it's starting parenthesis to the end and after the whole loop is completed we return
# the result in a string format using join.

# Approach 1 TC: (loop till N)* (Reversing the string of length N) = O(N)*O(N) = O(N^2)
# Approach 2 TC: (Loop till N for opposite index pair) + (Loop till N to find the reverse string) = O(N + N) = O(N) 

class Solution:
    def reverseParentheses(self, s: str) -> str:
        indx_stack = deque()
        opp_pairs = [-1]*len(s)
        # res = []
        
        # for char in s:
        #     if char == '(':
        #         indx_stack.append(len(res))
            
        #     elif char == ')':
        #         start = indx_stack.pop()
        #         res[start:] = res[start:][::-1] #Reverse the String from earliest openning parentheses to the present closing parentheses
        #     else:
        #         res.append(char)
        # return "".join(res)

        # Apporach 2
        for i in range(len(s)):
            if s[i] == '(':
                indx_stack.append(i)
            elif s[i] == ')':
                start = indx_stack.pop()
                opp_pairs[i] = start
                opp_pairs[start] = i
        print(opp_pairs)

        curr_indx = 0
        curr_dir = 1  # for the direction of pointer movement (-1 or 1)
        res = ""

        while curr_indx < len(s):
            char = s[curr_indx]

            if char in "()":
                curr_indx = opp_pairs[curr_indx]
                curr_dir *= -1
            else:
                res = res + char
            
            curr_indx += curr_dir
        return res


