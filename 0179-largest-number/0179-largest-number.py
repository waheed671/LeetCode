class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        
        nums = list(map(str, nums))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare))
        
        # If the largest is "0", answer must be "0"
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)
