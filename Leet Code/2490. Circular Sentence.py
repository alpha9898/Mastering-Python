class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for i in range(len(words) - 1):
            last_char = words[i][-1]
            first_char_next = words[i+1][0]
            if last_char != first_char_next:
                return False
        
        last_char = words[-1][-1]
        first_char_first = words[0][0]
        
        if last_char != first_char_first:
            return False
        
        return True