class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            elif num > pq[0]:
                heapq.heapreplace(pq, num)
        return pq[0]