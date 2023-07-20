class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count =0
        for item in details:
            f = int(item[11:13])
            if f > 60:
                count += 1
        return count