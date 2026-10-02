class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        
        return encoded

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            l = i
            while s[l] != "#":
                l += 1
            
            length = int(s[i:l])
            dec.append(s[l+1 : l + 1 + length])    
            i = l + 1 + length
            
        return dec
