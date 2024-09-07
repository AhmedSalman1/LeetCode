class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for ch in string:
                count[ord(ch) - ord('a')] += 1
            h_map[tuple(count)].append(string)
        
        return h_map.values()