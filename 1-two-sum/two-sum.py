class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()  # Set to store the numbers seen so far
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # Return the indices of the complement and the current number
                return [nums.index(complement), i]
            seen.add(num)  # Add the current number to the set of seen numbers
        
        # No solution found
        return None
