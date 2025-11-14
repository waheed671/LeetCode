class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define mappings of integer values to Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""
        for i in range(len(val)):
            # Repeat while num is large enough
            while num >= val[i]:
                num -= val[i]
                roman += syms[i]
        return roman
