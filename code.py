class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        INF = n + 1
    
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = INF # marks zero or negative numbers as infinitive positive numbers
                
        for i in range(n):
            x = abs(nums[i]) - 1 # use index start with zero
            if x < n:
                nums[x] = -abs(nums[x]) # mark `x` as visited by marking `nums[x]` as negative
                    
        for i in range(n):
            if nums[i] > 0: # if nums[i] is positive -> number (i+1) is not visited.
                return i + 1
        return n + 1
