# 3, 2, 3

# 11, 10, 11
# 32  

# 11

# majority element is n
# arr[:i], arr[i:]
# if arr[:i].count(n) == len(arr[:i])//2
# then arr[i:].count(n) > len(arr[i:])//2

# len(arr[i:]) == 3
# ab a
# aab
# ba a


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # num_freq = dict()
        # for num in nums:
        #     num_freq[num] = num_freq.get(num, 0) + 1
        #     if num_freq[num] > len(nums) // 2: 
        #         return num
        count = 0
        for num in nums:
            if count == 0: 
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
