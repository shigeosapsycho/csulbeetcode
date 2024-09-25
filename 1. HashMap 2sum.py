class Solution(object):
    def twoSum(self, nums, target):
        seen = {} # Creates a hash map (otherwise known as an empty dictonary) to store numbers
        for i in range(len(nums)): # This for loop will take every number in the list 'nums'
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i 
#42 ms
# No return function is needed since the LeetCode problem is guaranteed one solution for every list.
