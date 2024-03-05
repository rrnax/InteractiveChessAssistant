import chess

class Game:
    _instance = None
    chess_board = chess.Board()
    moves_options_history = []
    advantage_history = []
    last_move = "0000"

    #Singleton for only one possible instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    #Can start from all valid fen notation
    def __init__(self, fen=chess.STARTING_FEN):
        try:
            print("Sat start position...")
            self.chess_board.set_fen(fen)
            print(self.chess_board)
        except ValueError:
            print("Cannot convert fen, setting default starting position...")
            self.chess_board = chess.STARTING_FEN

    def make_move_uci(self, uci):
        try:
            current_move = chess.Move.from_uci(uci)
            if current_move in self.chess_board.legal_moves:
                self.chess_board.push(current_move)
                if self.chess_board.is_checkmate():
                    return "Checkmate"
                elif self.chess_board.is_stalemate():
                    return "Draw"

                    return "Check"
                else:
                    print(self.chess_board)
                    return "next move"
            else:
                return "not allow"
        except chess.InvalidMoveError:
            print("Not propirate move!")


