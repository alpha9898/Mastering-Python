class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        capitalized_words = []
        for word in words:
            if len(word) == 1 or len(word) == 2:
                capitalized_words.append(word.lower())
            else:
                capitalized_words.append(word.capitalize())

        capitalized_title = " ".join(capitalized_words)
        return capitalized_title