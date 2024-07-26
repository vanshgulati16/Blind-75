Approach: We wi ll use Dijkstra algorithm here with bit tweaking, instead for finding the shortest path for which we used hashset we will be using set for keeping the node visited. 
But the only condition is we will check for the threshold before adding the neighbour distance and neighbour into the priority heap.

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)

        for v1, v2, dist in edges:
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))

        def dijsktra(src):
            heap = [(0, src)] #dist, node. distance is first as we priority of distance is more for the approach here
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)

                for nei, dist2 in adj[node]:
                    nei_dist = dist2 + dist
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))

            return len(visit) -1 # to remove the initial 0 as src node can't visit itself.
        
        res, min_count = -1, float("inf")

        for src in range(n):
            count = dijsktra(src)
            # as we are going through the node in ascending order and we need to return the node with a greater node value for the smallest number of neighbors that's why we have equal sign.
            if count <= min_count:
                res, min_count = src, count
        return res

