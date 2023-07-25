class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0
        for char in s:
            if char == "L":
                late += 1
                if late > 2:
                    return False
            else:
                late = 0  # Reset the late count when there's no 'L'
                if char == "A":
                    absent += 1
                    if absent > 1:
                        return False
        return True