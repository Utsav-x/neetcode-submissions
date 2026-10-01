class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        ans = []
        for i,n in enumerate(nums):
            diff = target - n
            
            if diff in s:
                ans.append(s[diff])
                ans.append(i)
                return ans
            
            s[n] = i

