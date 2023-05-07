class Piece:
    def __init__(self, color, piece_class):
        self.color = color
        self.piece_class = piece_class
        self.icon = None
        if color == "black":
            if piece_class == "rook":
                self.icon = "♖"
            elif piece_class == "knight":
                self.icon = "♘"
            elif piece_class == "bishop":
                self.icon = "♗"
            elif piece_class == "queen":
                self.icon = "♕"
            elif piece_class == "king":
                self.icon = "♔"
            elif piece_class == "pawn":
                self.icon = "♙"
        elif color == "white":
            if piece_class == "rook":
                self.icon = "♜"
            elif piece_class == "knight":
                self.icon = "♞"
            elif piece_class == "bishop":
                self.icon = "♝"
            elif piece_class == "queen":
                self.icon = "♛"
            elif piece_class == "king":
                self.icon = "♚"
            elif piece_class == "pawn":
                self.icon = "♟"
        self.current_pos = (0, 0)
        self.isAlive = True

    def move(self, newX, newY):
        # verify bishop movement
        canMove = False

        if self.color == "black":
            if self.current_pos[0] + 1 == newX and self.current_pos[1] + 1 == newY:
                canMove = True
            elif self.current_pos[0] + 1 == newX and self.current_pos[1] - 1 == newY:
                canMove = True
            elif self.current_pos[0] - 1 == newX and self.current_pos[1] + 1 == newY:
                canMove = True
            elif self.current_pos[0] - 1 == newX and self.current_pos[1] - 2 == newY:
                canMove = True


        if canMove:
            self.current_pos = (newX, newY)