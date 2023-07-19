class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        map = {
            'a1': False, 'b1': True, 'c1': False, 'd1': True, 'e1': False, 'f1': True, 'g1': False, 'h1': True,
            'a2': True, 'b2': False, 'c2': True, 'd2': False, 'e2': True, 'f2': False, 'g2': True, 'h2': False,
            'a3': False, 'b3': True, 'c3': False, 'd3': True, 'e3': False, 'f3': True, 'g3': False, 'h3': True,
            'a4': True, 'b4': False, 'c4': True, 'd4': False, 'e4': True, 'f4': False, 'g4': True, 'h4': False,
            'a5': False, 'b5': True, 'c5': False, 'd5': True, 'e5': False, 'f5': True, 'g5': False, 'h5': True,
            'a6': True, 'b6': False, 'c6': True, 'd6': False, 'e6': True, 'f6': False, 'g6': True, 'h6': False,
            'a7': False, 'b7': True, 'c7': False, 'd7': True, 'e7': False, 'f7': True, 'g7': False, 'h7': True,
            'a8': True, 'b8': False, 'c8': True, 'd8': False, 'e8': True, 'f8': False, 'g8': True, 'h8': False,
        }
        
        return map[coordinates]