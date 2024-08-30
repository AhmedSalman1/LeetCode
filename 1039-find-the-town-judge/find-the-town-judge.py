class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        trust_score = [0] * (n + 1)

        for p1, p2 in trust:
            trust_score[p1] -= 1
            trust_score[p2] += 1

        for person in range(1, n + 1):
            if trust_score[person] == n - 1:
                return person
        
        return -1
        