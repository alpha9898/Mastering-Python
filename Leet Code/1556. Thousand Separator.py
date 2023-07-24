class Solution:
    def thousandSeparator(self, n: int) -> str:
        x = str(n)
        return re.sub(r'(?<=\d)(?=(\d{3})+$)', '.', x)