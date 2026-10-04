class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = "".join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(sp) - 1

        while l < r:
            if sp[l] != sp[r]:
                return False
            l += 1
            r -= 1
        return True