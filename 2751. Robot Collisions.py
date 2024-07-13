# Question: https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2024-07-13

# Approach: for approach refer to this video(https://www.youtube.com/watch?v=kLjAWG1Je-c),The algorithm simulates robot collisions on a line. It sorts robots by position and processes 
# them sequentially. A stack tracks potential collisions, handling robots moving right and left differently. When a left-moving robot encounters right-moving robots, collisions are simulated. 
# In each collision, the robot with lower health is eliminated, and the survivor loses one health point. If healths are equal, both robots are eliminated. This process continues until no more 
# collisions are possible. The final step returns the health values of surviving robots in their original order, efficiently resolving all collisions in a single pass through the sorted list.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted(zip(positions, healths, directions, range(n)))
        stack = []

        for pos, health, direction, index in robots:
            if direction == 'R' or not stack or stack[-1][2] == 'L':
                stack.append([pos, health, direction, index])
                continue

            while stack and stack[-1][2] == 'R':
                if health > stack[-1][1]:
                    health -= 1
                    stack.pop()
                elif health < stack[-1][1]:
                    stack[-1][1] -= 1
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append([pos, health, direction, index])
        return [health for _, health, _, _ in sorted(stack, key=lambda x: x[3])]
