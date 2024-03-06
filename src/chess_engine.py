import os
import asyncio
import chess.engine

class ChessEngine:
    _instance = None
    stockfish_path = os.path.join('../engines/stockfish', 'stockfish-windows-x86-64.exe')
    lc0 = ''
    transport = None
    engine = None
    engine_limits = chess.engine.Limit()
    results_amount = None
    engine_name = None
    opponent = None

    def __init__(self, engine_name="stockfish", depth="20"):
        try:
            self.engine_limits.depth=depth
            if engine_name == "stockfish":
                self.transport, self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path)
                self.set_opponent()
                self.engine.send_opponent_information(opponent=self.opponent)
            elif engine_name == "lco":
                self.transport, self.engine = chess.engine.popen_uci(self.lc0)
        except Exception:
            print("Cannot open connect to engine...")

    def __del__(self):
        self.engine.quit()
    # Setters
    def set_think_time(self, time_sec):
        self.engine_limits.time = time_sec

    def set_depth(self, amount):
        self.engine_limits.depth = amount

    def set_results_amount(self, amount):
        self.results_amount = amount

    def set_engine(self, engine_name):
        self.engine_name = engine_name

    def set_opponent(self, title="None", elo=2200, engine_opponent=False):
        self.opponent = chess.engine.Opponent(title=title, rating=elo, is_engine=engine_opponent)

    def engine_turn(self, board):
        if board is None:
            return None
        else:
            result = self.engine.play(board, self.engine_limits)
            print(result)
            return result



    async def move_analyze(self, chess_board):
        if self.engine_name == 'stockfish':
            transport, engine = await chess.engine.popen_uci(self.stockfish)
        elif self.engine_name == 'lc0':
            transport, engine = await chess.engine.popen_uci(self.lc0)

        results = await self.engine.analysis(chess_board, self.engine_limits, multipv=self.results_amount)
        await self.engine.quit()
        return results