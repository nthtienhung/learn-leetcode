n = 899 

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
        output = 0
        while n:
            lastdigit = n % 10
            output += lastdigit * lastdigit
            print(output)
            n = n // 10
        return output

instance = Solution()
print(instance.isHappy(n))
print(2 //10)
