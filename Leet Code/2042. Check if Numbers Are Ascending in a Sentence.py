class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = []
        x = s.split()
        for item in x:
            if item.isdigit():
                num.append(int(item))
                
        for n in range(1, len(num)):
            if num[n] <= num[n - 1]:
                return False
        return True