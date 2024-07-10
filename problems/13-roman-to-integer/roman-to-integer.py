class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        prev_value = 0
        for ch in reversed(s):
            curr_value = roman_values[ch]
            if curr_value >= prev_value:
                value += curr_value
            else:
                value -= curr_value
            prev_value = curr_value
        return value