class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        
        
        s_hmap, t_hmap = {}, {}

        for i in range(len(s)):
            s_hmap[s[i]] = s_hmap.get(s[i], 0) + 1
            t_hmap[t[i]] = t_hmap.get(t[i], 0) + 1

        return s_hmap == t_hmap    