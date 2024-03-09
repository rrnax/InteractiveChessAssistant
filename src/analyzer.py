import chess_engine


class Analyzer:
    _instance = None
    chess_board = None
    current_advantage = None
    white_best_moves = []
    black_best_moves = []
    using_engine = None

    # Class as singleton
    def __init__(self):
        self.using_engine = chess_engine.ChessEngine()





