class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        
        blocks = []
        while len(number) > 4:
            blocks.append(number[:3])
            number = number[3:]
        
        if len(number) == 4:
            blocks.append(number[:2])
            blocks.append(number[2:])
        else:
            blocks.append(number)
        
        return '-'.join(blocks)