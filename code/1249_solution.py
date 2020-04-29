class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        capacity = s.count(')')
        opened = 0
        for char in s:
            if char == '(':
                if opened == capacity: continue              
                opened += 1
            elif char == ')':
                capacity -= 1
                if not opened: continue
                opened -= 1
            result.append(char)
        return ''.join(result)
        