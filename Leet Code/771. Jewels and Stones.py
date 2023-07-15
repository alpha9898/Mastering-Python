class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in jewels:
            for charr in stones:
                if charr == char:
                    count += 1
        return count