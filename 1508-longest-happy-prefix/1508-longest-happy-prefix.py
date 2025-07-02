class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n  # Longest Prefix Suffix array
        length = 0  # length of the previous longest prefix suffix

        for i in range(1, n):
            while length > 0 and s[i] != s[length]:
                length = lps[length - 1]
            if s[i] == s[length]:
                length += 1
                lps[i] = length

        return s[:lps[-1]]
