from functools import lru_cache

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         pq = []
#         dist = lambda x: x[0] ** 2 + x[1] ** 2
#         for p in points:
#             d = dist(p)
#             if len(pq) < K:
#                 heapq.heappush(pq, (-d, p))
#             elif d < -pq[0][0]:
#                 heapq.heapreplace(pq, (-d, p))
#         return [t[1] for t in pq]
        @lru_cache(maxsize=len(points))
        def dist(x, y):
            return x ** 2 + y ** 2            
        
        def swap(i, j):
            points[i], points[j] = points[j], points[i]
    
        def partition(l, r):
            m = (l + r) // 2
            pivot = dist(*points[m])
            swap(l, m)
            i, j = l, r
            while i < j:
                while i < r and dist(*points[i]) <= pivot: i += 1
                while j > l and dist(*points[j]) >= pivot: j -= 1
                if i < j and dist(*points[i]) > dist(*points[j]):
                    swap(i, j)
            swap(j, l)
            return j
    
        def sort(l, r, k):
            m = partition(l, r)
            d = m - l + 1
            if d == k: return
            elif d < k: sort(m + 1, r, k - d)
            else: sort(l, m - 1, k)
        
        sort(0, len(points) - 1, K)
        return points[:K]