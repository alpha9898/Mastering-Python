class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = []
        x = text.split()
        for i in range(2, len(x)):
            if x[i - 2] == first and x[i - 1] == second:
                words.append(x[i])
        return words
