class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        my_list = []
        for char1, char2 in zip(word1, word2):
            my_list.append(char1)
            my_list.append(char2)

        my_list.extend(word1[len(word2):])
        my_list.extend(word2[len(word1):])

        h = "".join(my_list)
        return h