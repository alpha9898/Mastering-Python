class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch) 
        if index == -1:
            return word
        reversed_segment = word[:index + 1][::-1]
        result = reversed_segment + word[index + 1:]
        return result
