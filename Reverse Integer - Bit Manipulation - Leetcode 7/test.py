class Solution:
    #half mine, half neetcode solution
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)

        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x > 0:
            lastdigit = x % 10
            x = int(x/10)
            
            #part from neetcode solution 
            if(res > MAX // 10 or 
            (res == MAX // 10 and lastdigit >= MAX % 10 )):
                return 0
            if(res < MIN // 10 or
            (res == MIN // 10 and lastdigit <= MIN % 10)):
                return 0

            res = res * 10 + lastdigit

        if negative:
            res = -res
        return res