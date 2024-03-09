# import asyncio
# import chess.engine
import game
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
menu1 = "1 - graj,"
menu2 = "2 - zakończ grę,"
menu4 = "3 - od nowa,"
menu3 = "4 - dalej"
print("START PROGRAMU")

while True:
    print(menu1 + menu2)
    decision = input("Co chcesz zrobić? ")
    gra = game.Game()
    if decision == "1":
        print("No to gramy!")
        decision3 = input("Wybierz kolor bierek 5 - biale, 6 - czarne")

        if decision3 == "5":
            gra.setup(game_type="simple", user_side="white")
        elif decision3 == "6":
            gra.setup(game_type="simple", user_side="black")
        while True:
            print(menu2 + menu4 + menu3)
            decision2 = input()
            if decision2 == "2":
                print("KONCZYMY")
                gra.close()
                exit(0)
            elif decision2 == "3":
                print("OD NOWA")
                break
            elif decision2 == "4":
                result = gra.game_turn()
                if result:
                    break
                else:
                    continue
            else:
                print("Zły ruch jeszcze raz!")

    elif decision == "2":
        print("KONCZYMY")
        gra.close()
        exit(0)
    else:
        continue

# gra = game.Game()
# print(gra.chess_board)
#
#
# while gra.state == 'play':
#     wej = input(gra.get_turn() + " podaj ruch: ")
#     gra.make_move_uci(wej)
