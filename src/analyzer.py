import chess_engine
import multiprocessing as mp


class Analyzer:
    _instance = None
    chess_board = None
    current_advantage = None
    white_best_moves = []
    black_best_moves = []
    using_engine = None

    # result_queue = mp.Queue()
    # process_pool = mp.Pool()

    def __init__(self):
        self.using_engine = chess_engine.ChessEngine()
        p1 = mp.Process(target=czwds, args=(10,))
        p2 = mp.Process(target=czwds, args=(1,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print("DONE")


def czwds(lk):
    print("result: ", lk * lk)
