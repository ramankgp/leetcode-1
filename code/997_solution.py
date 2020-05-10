# N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# person       1  2  3  4
# in_edges =  [0, 0, 3, 2]
# out_edges = [2, 2, 0, 1]
#                    ^
# out_edges[judge] == 0
# in_edges[judge] = N-1

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # in_edges = collections.defaultdict(int)
        # out_edges = collections.defaultdict(int)
        trusts = [0] * (N+1)
        for frm, to in trust:
            # in_edges[to] += 1
            # out_edges[frm] += 1
            trusts[to] += 1
            trusts[frm] -= 1
        for person in range(1, N+1):
            # if out_edges[person] == 0 and in_edges[person] == N-1:
            # if in_edges[person] - out_edges[person] == N-1:                
            if trusts[person] == N-1:
                return person
        return -1
