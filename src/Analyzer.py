import chess
class Analyzer:
    _instance = None
    chess_board = None
    current_advantage = None
    white_best_moves = []
    black_best_moves = []

    # Class as singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance



