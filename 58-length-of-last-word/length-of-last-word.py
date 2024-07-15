class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0

        for i in s[::-1]:
            if i == ' ':
                if cnt >= 1:
                    return cnt
            else:
                cnt += 1
        return cnt