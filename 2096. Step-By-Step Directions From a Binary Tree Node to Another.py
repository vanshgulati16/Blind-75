#Question: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/?envType=daily-question&envId=2024-07-16

# Approach: transforms the binary tree into a graph using breadth-first search (BFS), creating bidirectional connections between nodes with appropriate direction labels ('L', 'R', 'U'). 
# It stores these connections in a defaultdict, where each node's value maps to a list of its neighbors and corresponding directions. Then, it performs another BFS starting from the start node 
# to find the shortest path to the destination. This second BFS uses a queue to track nodes and their paths, and a visited set to avoid cycles. It explores the graph level by level, appending 
# directions to the path as it goes. When the destination is reached, it returns the accumulated path. This approach efficiently handles any path in the tree, including those that go up and then 
# down different branches, with a time and space complexity of O(n), where n is the number of nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = collections.defaultdict(list)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.left.val].append((node.val, 'U'))
                graph[node.val].append((node.left.val, 'L'))

                queue.append(node.left)
            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))

                queue.append(node.right)
        
        queue = deque([(startValue, "")])
        visited = set()

        while queue:
            cur_val, cur_path = queue.popleft()

            if cur_val in visited:
                continue
            visited.add(cur_val)

            if cur_val == destValue:
                return cur_path
            else:
                for child, direction in graph[cur_val]:
                    if child not in visited:
                        queue.append([child, cur_path + direction])
