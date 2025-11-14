class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:      # If n is odd, multiply result by x
                result *= x
            x *= x               # Square x
            n //= 2              # Divide n by 2
        
        return result

        