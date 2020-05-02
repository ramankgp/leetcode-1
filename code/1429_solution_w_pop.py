# 23325
#     ^
#     first unique

# pop(2)

# 3325
#   ^
#   first unique

#  nxt
# -------------
# |           |
# |           V
# 2<->3<->3<->2<->5
# ^           |   ^
# -------------   first unique
#     pre 
    
class Node:
    def __init__(self, value, seq, pre, nxt):
        self.value = value
        self.seq = seq
        self.pre = pre
        self.nxt = nxt
    
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.seen = dict()
        self.loc = 0
        self.seq = 0
        for value in nums: self.add(value)

    def showFirstUnique(self) -> int:
        while self.loc < len(self.queue):
            node = self.queue[self.loc]
            if node.pre or node.nxt: self.loc += 1
            else: return node.value
        return -1
        
    def add(self, value: int) -> None:
        node = Node(value, self.seq, None, None)
        if value in self.seen:
            node.pre = self.seen[value]
            self.seen[value].nxt = node
        self.seen[value] = node
        self.queue.append(node)
        self.seq += 1
        
    def pop(self):
        node = self.queue.popleft()
        if self.seen[node.value] == node:
            self.seen.pop(node.value)
        if node.nxt:
            node.nxt.pre = None
            if not node.nxt.nxt:
                self.loc = min(self.loc - 1, node.nxt.seq - node.seq)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)