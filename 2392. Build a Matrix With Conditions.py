# Question: https://leetcode.com/problems/build-a-matrix-with-conditions/?envType=daily-question&envId=2024-07-21

# Approach: for approach we need to see this video(https://www.youtube.com/watch?v=khTKB1PzCuw). In short, we are using topological sort here on the rows and col conditions and then reversing
# the order of sort but to do the topologcial sort we need to traverse the graph using DFS approach. In the end we are returning a matrix(KxK), using the order of topological sort for rows 
# and columns.

# Study: Topological sort and DFS

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            
            visit.add(src)
            path.add(src)
            
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            # print("order: ", order)
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adj = defaultdict(list)

            for src, dst in edges:
                # print("source: ", src)
                # print("destination: ", dst)
                adj[src].append(dst)
            visit, path = set(), set()
            order = []

            for src in range(1,k+1):
                if not dfs(src, adj, visit, path, order):
                    return[]
            return order[::-1]  #reverse the output as we storing the leaf nodes first.
        
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []
        
        val_to_row = {n:i for i,n in enumerate(row_order)}
        val_to_col = {n:i for i,n in enumerate(col_order)}
        res = [[0]*k for _ in range(k)]

        for num in range(1, k+1):
            r,c = val_to_row[num], val_to_col[num]
            res[r][c] = num
        return res
