class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Main idea is find 2 equal numbers then 
        # see if there distance is less than k
        # However, iterate from left to right
        # - If the number is not in the dict(), then insert it
        # - Else : we know that a number is in the dict called nums[i]
        # and we encounter nums[j]==nums[i],
        # We check if abs(i-j) <= k
        #   + If yes, then return
        #   + Else, we update that new position to our dict()
        #     --> The reason for this is to reduce the distance in the future
        #     --> Suppose we have position i<j and abs(i-j)>k (ofc nums[i]==nums[j])
        #     --> update mydict[nums[i]]=j so that if we encounter a new l with nums[j]=nums[l]
        #     --> abs(l-i) < abs(l-i)
        mydict = dict()
        for i in range(len(nums)):
            if nums[i] in mydict:
                if (abs(mydict[nums[i]]-i)<=k): return True
            mydict[nums[i]]=i
        return False
        