class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        l = str(x)
        
        # Check if the reversed string is equal to the original string
        return l[::-1] == l
