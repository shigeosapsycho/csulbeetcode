# from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        NumberSet = set() # Create an empty set to track seen numbers. Sets ignore duplicate values automatically.

        for num in nums: # Loop through the list of numbers
            if num in NumberSet: # If the number is already in the set (duplicate found), return True
                return True
            else: # If the number is not in the set, add it to the set
                NumberSet.add(num)
        return False # Return False if no duplicates are found after the loop
    
# Time complexity: O(n) since we loop through all n elements in the list, and checking/adding in a set is O(1) on average.

"""
# Create an instance of the Solution class
solution = Solution()

numbers = [1,2,3,1]
print(solution.containsDuplicate(numbers))

numbers = [1,2,3,4]
print(solution.containsDuplicate(numbers))

numbers = [1,1,1,3,3,4,3,2,4,2]
print(solution.containsDuplicate(numbers))
"""