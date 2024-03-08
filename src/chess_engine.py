import os
import asyncio
import chess.engine


class ChessEngine:
    _instance = None
    transport = None
    engine = None
    engine_limits = chess.engine.Limit()
    results_amount = None
    opponent = None

    # Setting first attributes for engine
    def __init__(self, engine_name="stockfish", depth="20"):
        self.set_depth(depth)
        asyncio.run(self.engine_selection(engine_name=engine_name))

    # Setters
    def set_think_time(self, time_sec):
        self.engine_limits.time = time_sec

    def set_depth(self, amount):
        self.engine_limits.depth = amount

    def set_results_amount(self, amount):
        self.results_amount = amount

    def set_opponent(self, title="None", elo=2200, engine_opponent=False):
        self.opponent = chess.engine.Opponent(name="user", title=title, rating=elo, is_engine=engine_opponent)

    # Engine selection or input
    async def engine_selection(self, engine_name):
        if engine_name == "stockfish":
            path = os.path.join('../engines/stockfish', 'stockfish-windows-x86-64.exe')
            self.transport, self.engine = await chess.engine.popen_uci(path)
        elif engine_name == "lc0":
            print()
        self.set_opponent()
        await self.engine.send_opponent_information(opponent=self.opponent)
        print("Ustaiwono silnik")

    def close_engine(self):
        self.engine.quit()

    # def engine_turn(self, board):
    #     if board is None:
    #         return None
    #     else:
    #         result = self.engine.play(board, self.engine_limits)
    #         print(result)
    #         return result
    #
    # async def move_analyze(self, chess_board):
    #     if self.engine_name == 'stockfish':
    #         transport, engine = await chess.engine.popen_uci(self.stockfish)
    #     elif self.engine_name == 'lc0':
    #         transport, engine = await chess.engine.popen_uci(self.lc0)
    #
    #     results = await self.engine.analysis(chess_board, self.engine_limits, multipv=self.results_amount)
    #     await self.engine.quit()
    #     return results
