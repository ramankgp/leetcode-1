from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-cnt, ch) for ch, cnt in Counter(S).items()]
        heapq.heapify(pq)
        if -pq[0][0] > (len(S) + 1) / 2: return ""
        
        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 != -1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 != -1: heapq.heappush(pq, (nct2 + 1, ch2))
        return "".join(ans) + (pq[0][1] if pq else "")