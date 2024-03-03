import chess

class VirtualBoard:
    _instance = None
    console_look = []

    # Class as singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, fen=chess.STARTING_FEN):
        self.board = chess.Board(fen)
        for row in range(18):
            if row % 2 == 0:
                if row == 0:
                    self.console_look.append([" ", "|", "A", "|", "B", "|", "C", "|", "D", "|", "E", "|", "F", "|", "G", "|", "H"])
                else:
                    self.console_look.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
            else:
                return 1

    # def print_board(self):
