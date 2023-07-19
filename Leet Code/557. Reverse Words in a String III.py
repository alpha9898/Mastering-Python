class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split()
        rt = [string[::-1] for string in t]
        x = ' '.join(rt)
        return x