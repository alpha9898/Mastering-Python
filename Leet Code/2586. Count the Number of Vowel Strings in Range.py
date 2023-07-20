from typing import List

class Solution:
    def is_vowel_string(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return word[0] in vowels and word[-1] in vowels

    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            if self.is_vowel_string(words[i]):
                count += 1
        return count
