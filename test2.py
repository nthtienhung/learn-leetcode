
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 0 or n > 2147483647:
            return "invalid input"
        totalOf1bits = 0
        binary0b = bin(n)
        binary = binary0b[2::]
        for c in binary:
            if c == '1' :
                totalOf1bits += 1
        return totalOf1bits
s = Solution()
print(s.hammingWeight(2147483645))