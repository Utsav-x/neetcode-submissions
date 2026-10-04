class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = "".join(char.lower() for char in s if char.isalnum())
        return sp == sp[::-1]