class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            # Shrink prefix until it matches the start of s
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
