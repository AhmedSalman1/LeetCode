class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for n in arr:
            dic[n] = 1 + dic.get(n, 0)

        return len(dic) == len(set(dic.values()))