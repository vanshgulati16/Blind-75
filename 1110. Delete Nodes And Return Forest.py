#Question: https://leetcode.com/problems/delete-nodes-and-return-forest/description/?envType=daily-question&envId=2024-07-17

#Approach: To delete nodes from a binary tree and return the resulting forest, we can use a depth-first search (DFS) traversal. First, convert the list of nodes to delete into a set for 
# efficient lookups. During the DFS, check if each node should be deleted. If a node is not to be deleted and is a root (either the original root or because its parent was deleted), add 
# it to the result list. Recursively process the left and right children, passing down whether the current node is deleted. This information helps determine if the children become new roots. 
# If a node is deleted, return None to its parent, effectively removing it from the tree. This single-pass approach efficiently handles deletion, forest creation, and result collection 
# simultaneously.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Convert to_delete to a hashset
        result = []
        
        def dfs(node, is_root):
            if not node:
                return None
            
            is_deleted = node.val in to_delete_set  # Use the hashset for lookup
            if is_root and not is_deleted:
                result.append(node)
            
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            
            return None if is_deleted else node
        
        dfs(root, True)
        return result
