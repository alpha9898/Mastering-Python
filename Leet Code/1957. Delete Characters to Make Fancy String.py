class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        fancy_string = s[0] 
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count < 3:
                fancy_string += s[i]

        return fancy_string
