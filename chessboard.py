board = [["▯▮▯▮▯▮▯▮",
          "▮▯▮▯▮▯▮▯",
          "▯▮▯▮▯▮▯▮",
          "▮▯▮▯▮▯▮▯",
          "▯▮▯▮▯▮▯▮",
          "▮▯▮▯▮▯▮▯",
          "▯▮▯▮▯▮▯▮",
          "▮▯▮▯▮▯▮▯"]
    ,
         ["♖♘♗♕♔♗♘♖",
          "♙♙♙♙♙♙♙♙",
          "▮▯▮▯▮▯▮▯",
          "▯▮▯▮▯▮▯▮",
          "▮▯▮▯▮▯▮▯",
          "▯▮▯▮▯▮▯▮",
          "♟♟♟♟♟♟♟♟",
          "♜♞♝♛♚♝♞♜"]]

class Space:
    def __init__(self, spaceX, spaceY, color):
        self.spaceX = spaceX
        self.spaceY = spaceY
        self.color = color
        self.isOccupied = False
        self.occupying_piece = None


    def __str__(self):
        if not self.isOccupied:
            if self.color == "white":
                return str("▮")
            elif self.color == "black":
                return str("▯")
        elif self.isOccupied:
            return str(self.occupying_piece)



class Board:
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.board_pattern = board[0]
        self.game_board = []

    def build_board(self):
        for row in self.board_pattern:
            for space in row:
                if space == "▯":
                    self.game_board.append(Space(self.startX, self.startY, "black"))
                if space == "▮":
                    self.game_board.append(Space(self.startX, self.startY, "white"))

    def draw_board(self):
        print("　" + "　".join(["a", "b", "c", "d", "e", "f", "g", "h"]))
        for i, space in enumerate(self.game_board):
            if i % 8 == 0:
                row_num = str(8 - i // 8)
                print(row_num + " ", end = '')
            print(str(space) + " ", end ='')
            if (i+1) % 8 == 0:
                print(row_num)

#
