class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquares(n)

        while slow != fast:
            fast = self.sumSquares(fast)
            fast = self.sumSquares(fast)
            slow = self.sumSquares(slow)
        
        return True if fast == 1 else False

    def sumSquares(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n = n // 10
        return res