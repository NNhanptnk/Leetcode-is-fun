class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # First while loop to find last white space at the end
        # Second while loop to count the length of the last word
        ans = 0
        pointer = len(s)-1
        
        while pointer >= 0:
            if s[pointer]!=' ':
                break
            pointer-=1

        while pointer >= 0:
            if s[pointer]==' ':
                break
            pointer-=1
            ans+=1
        return ans