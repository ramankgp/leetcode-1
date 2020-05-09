# i = end
# max_height = 3
# potential = 6
# accum = 1+1+2+1

# 1210121

class Solution:
    def trap(self, heights: List[int]) -> int:
        # max_height = potential = accum = 0
        # for height in heights:
        #     if height >= max_height:
        #         accum += potential
        #         potential = 0
        #         max_height = height
        #     else:
        #         potential += max_height - height
        # max_height = potential = 0
        # for height in reversed(heights):
        #     if height > max_height:
        #         accum += potential
        #         potential = 0
        #         max_height = height
        #     else:
        #         potential += max_height - height        
        # return accum
        accum = 0
        l, r = 0, len(heights) - 1
        l_max_height = r_max_height = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] >= l_max_height: l_max_height = heights[l]
                else: accum += l_max_height - heights[l]
                l += 1
            else:
                if heights[r] >= r_max_height: r_max_height = heights[r]
                else: accum += r_max_height - heights[r]
                r -= 1   
        return accum
                     