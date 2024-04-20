class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string contains valid parentheses.

        Args:
            s (str): The input string containing only parentheses ('()', '{}', '[]').

        Returns:
            bool: True if the parentheses are valid, False otherwise.
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                return False
        
        return not stack
