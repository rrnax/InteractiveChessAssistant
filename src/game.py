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
    using_engine = None

    # Singleton for only one possible instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    # Can start from all valid fen notation, setup necessary info
    def setup(self, fen=chess.STARTING_FEN, game_type="analyze", user_side="white"):
        try:
            self.chess_board.set_fen(fen)
        except ValueError:
            self.chess_board = chess.STARTING_FEN
        self.game_type = type
        self.state = "play"
        self.user_side = user_side
        self.using_engine = chess_engine.ChessEngine()

    # One turn is one white and one black move
    def game_turn(self):
        if self.game_type == "analyze":
            print("Ruch białych")
            print("Ruch czarnych")
        else:
            if self.user_side == "black":
                print("Ruch maszyny")
                print("Ruch gracza")
            elif self.user_side == "white":
                correct_move = True
                while correct_move:
                    move = input("Podaj ruch: ")
                    correct_move = self.move_uci(move)
                    if correct_move:
                        print("Zły rucj, jeszcze raz")
                print(self.chess_board)

                move = self.using_engine.engine_move(self.chess_board)
                self.chess_board.push(move)
                print(self.chess_board)

    def close(self):
        self.using_engine.close_engine()

    # All activities during move
    def move_uci(self, uci) -> bool:
        try:
            move = chess.Move.from_uci(uci)
            if move in self.chess_board.legal_moves:
                self.chess_board.push(move)
                return False
            else:
                return True
        except chess.InvalidMoveError:
            print("Cannot validate move from uci string...")
            return True

    # # Checking legal of mov and its result
    # def valid_move(self, move):
    #     if move in self.chess_board.legal_moves:
    #         self.chess_board.push(move)
    #         if self.chess_board.is_check():
    #             self.state = "check"
    #         elif self.chess_board.is_checkmate():
    #             self.state = "mate"
    #         elif self.chess_board.is_stalemate():
    #             self.state = "draw"
    #         elif self.chess_board.is_seventyfive_moves():
    #             self.state = "seventy-five"
    #         elif self.chess_board.is_fifty_moves():
    #             self.state = "fifty"
    #         elif self.chess_board.is_repetition():
    #             self.state = "draw"
    #         else:
    #             self.state = "play"
    #     else:
    #         self.state = "play"
    #
    # def get_turn(self):
    #     if self.chess_board.turn:
    #         return "white"
    #     else:
    #         return "black"

    # def start_engine(self, board):
    #     self.engine = chess_engine.ChessEngine()
    #     if  self.game_type is "single":
