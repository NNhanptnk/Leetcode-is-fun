This place is for storing useful trick when solving Leetcode problem 

### 1. Sort array base on another array

```python
def sort_array_base(list1 : List[int], list2: List[int]) -> None :
    # If we want to sort array list1 and want list 2 to follow 
    list1, list2 = zip(*sorted(zip(list1,list2)))    

```