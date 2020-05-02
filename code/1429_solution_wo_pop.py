class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = dict()
        self.seen = set()
        for value in nums: self.add(value)

    def showFirstUnique(self) -> int:
        return next(iter(self.queue.keys()), -1)

    def add(self, value: int) -> None:
        if value in self.seen:
            self.queue.pop(value, -1)
        else:
            self.seen.add(value)
            self.queue[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)