class Solution {
public:
    int reverse(int x) {
        long reversed = 0;  // use long to detect overflow

        while (x != 0) {
            int digit = x % 10;   // get last digit
            x /= 10;              // remove last digit

            reversed = reversed * 10 + digit;

            // check for overflow before returning
            if (reversed > INT_MAX || reversed < INT_MIN)
                return 0;
        }

        return static_cast<int>(reversed);
    }
};
