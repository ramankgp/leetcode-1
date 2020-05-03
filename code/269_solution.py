# ac
# ab

# a->c->b
# c->b->a
# c->a->b

# [
#   "wrt",
#   "wrf",   t->f
#   "er",    w->e
#   "ett",   r->t
#   "rftt"   e->r
# ]

# w->e->r->t->f
  
# [s,r,t,m,q,o,w]

# [w,o,q,m,t,r,s]

#   /--------->r-->s
#   |          ^   ^ 
#   |         /   /
# w-+------->t ---/
#   |
#   \------>o------->m
#           |        ^
#            \->q---/
# [w,o,t,r,s,q,m]

# z->x<->y
#    2->1     
        
# BFS with adj_list and in_degress,
# decrement in_degrees for nodes, when it reach 0
# mean we processes all the nodes before it, so we can put node on to ordering

# DFS with adj_list
# post order
# for nxt_node in adj_list[node]:
#   dfs(nxt_node)
# ordering.push_back(node)
# return ordering[::-1]
# need code in dfs function to handle cycles

# abc
# ab
    
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # construct the graph
        nodes = functools.reduce(set.union, map(set, words))
        out_edges = collections.defaultdict(list)
        # in_degrees = collections.defaultdict(int)
        ordering = []
        
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 == c2: continue
                # in_degrees[c2] += 1
                out_edges[c1].append(c2)
                break
            else:
                if len(w1) > len(w2): return ""
        
        # BFS 
        # queue = collections.deque(nodes.difference(in_degrees.keys()))
        # while queue:
        #     node = queue.popleft()
        #     ordering.append(node)
        #     for nxt_node in out_edges[node]:
        #         in_degrees[nxt_node] -= 1
        #         if not in_degrees[nxt_node]: queue.append(nxt_node)
        # return ''.join(ordering) if len(ordering) == len(nodes) else ""
        
        visited = dict()  # visited node -> cause cycle or not
        def dfs(node):
            if node not in visited:
                visited[node] = True
                for nxt_node in out_edges[node]:
                    if dfs(nxt_node): return True
                ordering.append(node)
                visited[node] = False
            return visited[node]
            
        while nodes:
            node = nodes.pop()
            has_cycle = dfs(node)
            if has_cycle: return ""
            else: nodes = nodes.difference(visited.keys())
        return ''.join(ordering[::-1])
    