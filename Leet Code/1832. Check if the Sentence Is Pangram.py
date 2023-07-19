class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for char in string.ascii_lowercase:
            if char not in sentence:
                return False
        return True