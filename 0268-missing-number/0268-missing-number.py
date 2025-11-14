class Solution:
    def missingNumber(self, nums):
        xor_sum = 0
        n = len(nums)
        
        for i in range(n + 1):
            xor_sum ^= i
        
        for num in nums:
            xor_sum ^= num
        
        return xor_sum
