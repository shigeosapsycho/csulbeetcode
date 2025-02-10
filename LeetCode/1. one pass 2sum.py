class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Initalize an empty HashMap
        i = 0 # Also initalize the counter to 0

        for n in nums: 
            diff = target - n # Calculate the difference between the target and the current number n
            if diff in prevMap: # We are looking if the difference (target - n) is in our hashmap
                return [prevMap[diff], i] # If the difference exists in the HashMap, return the indices of the two numbers that add up to the target
            prevMap[n] = i # Otherwise, if it is not in the hash map, we would add key n with value i
            i += 1 # Increment i by 1 to go through the input
        return []
