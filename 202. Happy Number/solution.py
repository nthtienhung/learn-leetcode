class Solution:
    #leetcode solution
    def isHappy(self, n: int) -> bool:
        sum_visited = set()

        while n not in sum_visited:
            sum_visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n):
        while n:
            output = 0
            lastdigit = n % 10
            output += lastdigit * lastdigit
            n = n // 10
            return output

