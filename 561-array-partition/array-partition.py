class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the input list in ascending order
        nums.sort()
        
        # Initialize a variable to store the sum of minimum pairs
        min_pair_sum = 0
        
        # Iterate through the sorted list and sum elements at even indices
        for i in range(0, len(nums), 2):
            min_pair_sum += nums[i]
        
        # Return the sum of minimum pairs
        return min_pair_sum
