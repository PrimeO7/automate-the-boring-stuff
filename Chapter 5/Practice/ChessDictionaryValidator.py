# ChessDictionaryValidator

from collections import Counter

def isValidChessBoard(board):
    # Check Kings
    king = Counter(board.values())
    if king['bking'] != 1 or king['wking'] != 1:
        return False
    
    # Check 16 pieces per player
    b = 0
    w = 0
    for colour in board.values():
    # Checks every Key for the String 'b' or 'w'
        if colour[0] == 'b':
            b += 1
        elif colour[0] == 'w':
            w += 1
    if b >= 17 or w >= 17:
        return False
    
    # Check 8 pawns per Player
    b = 0
    w = 0
    for piece in board.values():
    # Counts how many pawns of each colour are present
        if piece == 'bpawn':
            b += 1
        elif piece == 'wpawn':
            w += 1
    if b > 8 or w > 8:
        return False
    
    # Check Valid Spaces
    for position in board.keys():
        if len(position) != 2: 
            # checks if position value of the figure has valid lenght.
            return False
        if position[0] == 9:
            return False
        if position[1] not in 'abcdefgh':
            return False

    # Check Names
    for colour in board.values():
        if colour[0] not in 'bw':
            return False
        if colour[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen',
        'king']:
            return False

    return True


board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
'3e': 'wking'}

print(isValidChessBoard(board))
