class Solution:
    #geek4geek solution
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        #string s cant be modified, so need to assign to another var
        x = s.strip()

        for i in range(len(x)):
            if x[i] == " ":
                l = 0
            else:
                l += 1
        return l
    #neetcode solution
    def lengthOfLastWord1(self, s: str) -> int:
        #start from end
        #if spac
        i, word_leng = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            word_leng += 1
            i -= 1
        return word_leng