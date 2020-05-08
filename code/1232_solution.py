# y1=ax1+b
# y2=ax2+b

# (y2-y1)=a(x2-x1)

# a = (y2-y1)/(x2-x1)  x2 != x1
# b = y1 - x1 * (y2-y1) / (x2-x1)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x1 == x2: return all(x == x1 for x, _ in coordinates)
        a = (y2-y1)/(x2-x1) 
        b = y1 - x1 * (y2-y1) / (x2-x1)
        return all(y == a*x + b for x, y in coordinates)
