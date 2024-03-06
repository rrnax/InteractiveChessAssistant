import chess
import asyncio
import chess_engine

class Game:
    _instance = None
    chess_board = chess.Board()
    moves_options_history = []
    advantage_history = []
    last_move = "0000"
    state = None
    game_type = None
    user_side = None
    engine = None

    # Singleton for only one possible instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    # Can start from all valid fen notation
    def __init__(self, fen=chess.STARTING_FEN, type="analyze", side="white"):
        try:
            self.game_type = type
            print("Sat start position...")
            self.chess_board.set_fen(fen)
            self.state = "play"
            self.user_side = side
            self.engine = chess_engine.ChessEngine()
            if type == "single":
                if side == "black":
                    result = self.engine.engine_turn(self.chess_board)
                    self.chess_board.push(result.move)
                    print(self.chess_board)
        except ValueError:
            print("Cannot convert fen, setting default starting position...")
            self.game_type = type
            self.chess_board = chess.STARTING_FEN
            self.state = "play"

    # All activities during move
    def make_move_uci(self, uci):
        try:
            self.valid_move( chess.Move.from_uci(uci))
            print(self.chess_board)
            result = self.engine.engine_turn(self.chess_board)
            self.chess_board.push(result.move)
            print(self.chess_board)
        except chess.InvalidMoveError:
            print("Cannot validate move from uci string...")

    # Checking legal of mov and its result
    def valid_move(self, move):
        if move in self.chess_board.legal_moves:
            self.chess_board.push(move)
            if self.chess_board.is_check():
                self.state = "check"
            elif self.chess_board.is_checkmate():
                self.state = "mate"
            elif self.chess_board.is_stalemate():
                self.state = "draw"
            elif self.chess_board.is_seventyfive_moves():
                self.state = "seventy-five"
            elif self.chess_board.is_fifty_moves():
                self.state = "fifty"
            elif self.chess_board.is_repetition():
                self.state = "draw"
            else:
                self.state = "play"
        else:
            self.state = "play"

    def get_turn(self):
        if self.chess_board.turn:
            return "white"
        else:
            return "black"

    # def start_engine(self, board):
    #     self.engine = chess_engine.ChessEngine()
    #     if  self.game_type is "single":


