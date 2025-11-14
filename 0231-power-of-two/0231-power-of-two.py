class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # A power of two has exactly one '1' bit in binary and must be > 0
        return n > 0 and (n & (n - 1)) == 0

        