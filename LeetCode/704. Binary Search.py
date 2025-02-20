class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # Initalize 2 pointers, one at index 0 and the last index
        # len(nums) - 1 needed because the right pointer would go out of bounds

        while l <= r: # We do not want the left pointer to overlap the right pointer so we avoid this by doing <=
            m = l + ((r - l) // 2) # Calculate the middle point by calculating:
                                                                            # Lp + ((Rp - Lp) // 2)
            if nums[m] > target: # Run the midpoint through these test cases
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1
