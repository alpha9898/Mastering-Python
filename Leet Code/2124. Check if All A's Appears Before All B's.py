class Solution:
    def checkString(self, s: str) -> bool:
        x = s.lstrip("a")
        for char in x:
            if char=="a":
                return False 
        return True