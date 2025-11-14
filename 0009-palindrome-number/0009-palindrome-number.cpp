class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers and multiples of 10 (except 0) cannot be palindromes
        if (x < 0 || (x % 10 == 0 && x != 0)) 
            return false;
        
        int reversedHalf = 0;
        
        // Reverse only the second half of the number
        while (x > reversedHalf) {
            int digit = x % 10;
            reversedHalf = reversedHalf * 10 + digit;
            x /= 10;
        }
        
        // For even-length numbers: x == reversedHalf
        // For odd-length numbers: x == reversedHalf / 10 (middle digit ignored)
        return (x == reversedHalf) || (x == reversedHalf / 10);
    }
};
