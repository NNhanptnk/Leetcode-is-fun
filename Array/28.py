class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Brute force through by : for every position of haystack
        # check if needle is there
        # if yes then return that position
        # Continue until end, and return -1 if there's nothing match
        i = 0
        while i<=len(haystack)-len(needle):
            if (haystack[i:i+len(needle)]==needle): return i
            i+=1
        return -1      