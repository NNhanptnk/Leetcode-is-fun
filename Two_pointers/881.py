class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0,len(people)-1
        boat = 0
        while left<=right:
            ###1
            if people[left]+people[right]>limit:
                right-=1
                boat+=1
            else : 
                left+=1
                right-=1
                boat+=1
            ###2

        return boat
    
    def numRescueBoats2(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0,len(people)-1
        boat = 0
    
        # There's a way to write the code shorter
        # Optimize the above code between ###1 and ###2
        # Here goes :
        
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            boat+=1
        # The Logic : 
        # Since boat +=1 is updated in both if and else
        # and right-=1 is updated in both if and else

        return boat