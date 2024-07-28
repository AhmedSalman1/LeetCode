class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for op in operations:
            if op == '+' and len(score) >= 2:
                score.append(score[-1] + score[-2])

            elif op == 'D' and len(score) >= 1:
                score.append(score[-1] * 2)

            elif op == 'C' and len(score) >= 1:
                score.pop()
                
            else:
                score.append(int(op))
        
        return sum(score)