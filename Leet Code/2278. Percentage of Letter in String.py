class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        x=len(s)
        count = 0 
        for char in s:
            if letter == char:
                count +=1
        z = int(count / x * 100)
        return z