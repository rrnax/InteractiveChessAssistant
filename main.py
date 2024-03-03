# import asyncio
# import chess.engine
import VirtualBoard
#
# positon = "rnb1k1nr/ppppqppp/8/2b1p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 2 3"
#
# async def main() -> None:
#     transport, engine = await chess.engine.popen_uci(
#         r'D:\Dokumenty\Documents\Studies\Enginier\Repository\stockfish\stockfish-windows-x86-64.exe')
#     board = chess.Board(positon)
#
#     limits = chess.engine.Limit(depth=15)
#     # while not board.is_game_over():
#     result = await engine.analyse(board, limits, multipv=3)
#     for inf in result:
#         print(inf['score'], inf['pv'][1])
#
#     await engine.quit()
#
#
# asyncio.run(main())

myborda = VirtualBoard.VirtualBoard()