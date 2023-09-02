class Solution:
    def twoSum_two_pointers(self, numbers: List[int], target: int) -> List[int]:

        # Two pointers
        # Sum = numbers[left] + numbers[right]
        # Going from left to right : sum increase
        # Going from right to left : sum decrease
        left,right = 0,len(numbers)-1
        while left < len(numbers):
            if numbers[left]+numbers[right]==target : return [left+1,right+1]
            elif numbers[left]+numbers[right] > target :
                right-=1
            else : 
                left+=1
    
    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        # Binary search method
        def binary_search(num: int) -> int :
            low = 0
            high = len(numbers)-1
            while low <= high:
                mid = (low+high)//2
                if numbers[mid]==num : return mid
                elif numbers[mid] > num :
                    high = mid - 1
                else : 
                    low = mid + 1
            return -1
        
        for i in range(len(numbers)):
            temp = binary_search(target-numbers[i])
            if (temp != -1) and (temp != i):
                return [min(i+1,temp+1),max(i+1,temp+1)]
                # So weird, [4,5] is right but [5,4] is wrong, omg