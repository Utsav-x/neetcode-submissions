class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map = Counter(t)
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in t_map and t_map[i] > 0:
                t_map[i] -= 1
            else:
                return False
        
        return True
