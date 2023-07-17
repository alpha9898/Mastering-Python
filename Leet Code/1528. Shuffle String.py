class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restored = [''] * len(s)
        
        for i, char in enumerate(s):
            restored[indices[i]] = char
        
        return ''.join(restored)
