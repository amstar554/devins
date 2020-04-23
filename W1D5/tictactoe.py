gamecontinue = True
p1 = '1'
p2 = '2'
p3 = '3'
p4 = '4'
p5 = '5'
p6 = '6'
p7 = '7'
p8 = '8'
p9 = '9'
tictactoe1 = [f"[{p1}] [{p2}] [{p3}]"]
tictactoe2 = [f"[{p4}] [{p5}] [{p6}]"]
tictactoe3 = [f"[{p7}] [{p8}] [{p9}]"]

print(tictactoe1)
print(tictactoe2)
print(tictactoe3)

for x in range(10):
    if not gamecontinue:
        break
    if x == 9:
        print("It's a draw, sorry lads")
        break
    if x % 2 == 0:
        turn = "X"
    else:
        turn = "O"
    position = input(f"{turn} please enter the position your next move: ")
    if position == '1':
        p1 = turn
    if position == '2':
        p2 = turn
    if position == '3':
        p3 = turn
    if position == '4':
        p4 = turn
    if position == '5':
        p5 = turn
    if position == '6':
        p6 = turn
    if position == '7':
        p7 = turn
    if position == '8':
        p8 = turn
    if position == '9':
        p9 = turn

    tictactoe1 = [f"[{p1}] [{p2}] [{p3}]"]
    tictactoe2 = [f"[{p4}] [{p5}] [{p6}]"]
    tictactoe3 = [f"[{p7}] [{p8}] [{p9}]"]
    print(tictactoe1)
    print(tictactoe2)
    print(tictactoe3)

    if p1 == p2 == p3 or p4 == p5 == p6 or p7 == p8 == p9 or p1 == p5 == p9 or p3 == p5 == p7 or p1 == p4 == p7 or p2 == p5 == p8 or p3 == p6 == p9:
        print(f"{turn} is the winner!")
        gamecontinue = False

