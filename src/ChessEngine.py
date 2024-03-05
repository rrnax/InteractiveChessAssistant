import os
import asyncio
import chess.engine

class ChessEngine:
    _instance = None
    stockfish = os.path.join('../engines/stockfish', 'stockfish-windows-x86-64.exe')
    lc0 = ''
    engine_limits = chess.engine.Limit()
    results_amount = None
    engine_name = None

    # Class as singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    #Setters
    def set_think_time(self, time_sec):
        self.engine_limits.time = time_sec

    def set_depth(self, amount):
        self.engine_limits.depth = amount

    def set_results_amount(self, amount):
        self.results_amount = amount

    def set_engine(self, engine_name):
        self.engine_name = engine_name

    async def move_analize(self, chess_board):
        if self.engine_name is 'stockfish':
            transport, engine = await chess.engine.popen_uci(self.stockfish)
        elif self.engine_name is 'lc0':
            transport, engine = await chess.engine.popen_uci(self.lc0)

        results = await engine.analysis(chess_board, self.engine_limits, multipv=self.results_amount)
        await engine.quit()
        return results
