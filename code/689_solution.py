#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#              [6]
# max, loc = 13, 4
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#  [3] [3]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 3+3,[0,2]
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#    [3] [8]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 11=3+8>6,[0,3]
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#      [3] [13]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 16=3+13>11,[0,4]
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#        [8] [12]
# max_of_1, loc_of_1 = 8, [3]
# max_of_2, loc_of_2 = 20=12+8>16,[3,5]

# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#    [3] [8] [12]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 11,[0,3]
# max_of_3, loc_of_3 = 23,[0,3,5]

# max_of_i = max(max_of_i, max_of_{i-1}+sum_current_subarray_i)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int, m=3) -> List[int]:
        # Space and Time O(n)
        window_sums = [sum(nums[:k])]
        for i in range(1, len(nums)-k+1):
            window_sums.append(window_sums[-1]-nums[i-1]+nums[i+k-1])
        
        # Space O(m^2)
        max_sums = collections.defaultdict(lambda: [0, []])
        
        # Time O(m*n)
        for s in range(len(nums)-k*m+1): # O(n)
            for i in range(1,m+1): # O(m)
                l = s+(i-1)*k
                window_sum = window_sums[l]
                if window_sum + max_sums[i-1][0] > max_sums[i][0]:
                    max_sums[i][0] = window_sum + max_sums[i-1][0]
                    max_sums[i][1] = max_sums[i-1][1] + [l]
        return max_sums[m][1]
