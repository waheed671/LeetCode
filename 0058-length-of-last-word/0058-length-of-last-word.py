class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces
        s = s.rstrip()
        
        # Split the string by spaces
        words = s.split(' ')
        
        # Return the length of the last word
        return len(words[-1]) if words else 0

        