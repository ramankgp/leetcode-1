"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        deque = collections.deque([node])
        mapping = dict()
        while deque:  # Visit all the node
            nd = deque.popleft()  # bfs
            # nd = deque.pop()  # dfs
            if nd not in mapping: mapping[nd] = Node(nd.val)
            for nei in nd.neighbors:  # visit all the edges for the node
                if nei not in mapping:
                    mapping[nei] = Node(nei.val)
                    deque.append(nei)
                mapping[nd].neighbors.append(mapping[nei])
        return mapping[node]