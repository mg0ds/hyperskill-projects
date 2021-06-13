import random


def polegry():
    print("---------")
    print("| {} {} {} |".format(maciez["13"], maciez["23"], maciez["33"]))
    print("| {} {} {} |".format(maciez["12"], maciez["22"], maciez["32"]))
    print("| {} {} {} |".format(maciez["11"], maciez["21"], maciez["31"]))
    print("---------")

def drukuj_ruchy():
    print("\nMove code:")
    print("| 13 23 33 |")
    print("| 12 22 32 |")
    print("| 11 21 31 |")
    print()

def spr():
    wygrana = [[maciez["13"], maciez["12"], maciez["11"]], [maciez["23"], maciez["22"], maciez["21"]],
               [maciez["33"], maciez["32"], maciez["31"]], [maciez["13"], maciez["23"], maciez["33"]],
               [maciez["12"], maciez["22"], maciez["32"]], [maciez["11"], maciez["21"], maciez["31"]],
               [maciez["13"], maciez["22"], maciez["31"]], [maciez["33"], maciez["22"], maciez["11"]]]
    xwin = 0
    owin = 0
    for a in wygrana:
        wygranaspr = []
        for b in a:
            wygranaspr.append(b)
        if "XXX" in "".join(wygranaspr):
            xwin += 1
        elif "OOO" in "".join(wygranaspr):
            owin += 1
    if xwin >= 1:
        print("X wins\n")
        return "koniec"
    elif owin >= 1:
        print("O wins\n")
        return "koniec"
    elif runda >= 9 and xwin == 0 and owin == 0:
        print("Draw\n")
        return "koniec"


def start():
    while True:
        print("Options:")
        print("start [user/easy/medium] [user/easy/medium]")
        print("exit")
        start_choice = input("Input command: ").split(" ")
        if start_choice[0] == "exit":
            quit()
        else:
            if len(start_choice) == 3 and start_choice[0] == "start" and \
                    (start_choice[1] == "easy" or start_choice[1] == "user" or start_choice[1] == "medium") and \
                    (start_choice[2] == "medium" or start_choice[2] == "easy" or start_choice[2] == "user"):
                drukuj_ruchy()
                game(start_choice[1], start_choice[2])
            else:
                print("Bad parameters!")



def user_move(x_or_o):
    rxry = input("Enter the coordinates:").replace(" ", "")
    if rxry.isdigit():
        if int(rxry[0]) in range(1, 4) and int(rxry[1]) in range(1, 4) and len(rxry) == 2:
            if maciez[rxry] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                maciez[rxry] = x_or_o
                polegry()
                if spr() == "koniec":
                    start()
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

def ai_random_move():
    while True:
        ai_move = random.choice(["13", "23", "33", "12", "22", "32", "11", "21", "31"])
        if maciez[ai_move] == "_":
            return ai_move

def ai_medium_level(x_or_o):
    win = [[13, 12, 11], [23, 22, 21], [33, 32, 31], [13, 23, 33], [12, 22, 32], [11, 21, 31], [13, 22, 31],
           [33, 22, 11]]
    if x_or_o == "X":
        c = 1
    else:
        c = -1
    bbb = []
    for a in win:
        wygranaspr = 0
        poz = ""
        for b in a:
            if maciez[str(b)] == "X":
                wygranaspr += 1
            elif maciez[str(b)] == "O":
                wygranaspr += 5
            else:
                poz = b
        if wygranaspr == 2:
            bbb.append([1, poz])
        elif wygranaspr == 10:
            bbb.append([-1, poz])
    if len(bbb) == 0:
        return ai_random_move()
    else:
        for w in bbb:
            if w[0] == c:
                return str(w[1])
        for w in bbb:
            if w[0] != c:
                return str(w[1])

def ai_move(level, x_or_o):
    print(f'Making move level "{level}"')
    if level == "easy":
        maciez[ai_random_move()] = x_or_o
        polegry()
        if spr() == "koniec":
            start()
    elif level == "medium":
        maciez[ai_medium_level(x_or_o)] = x_or_o
        polegry()
        if spr() == "koniec":
            start()


def game(player_x, player_o):
    global maciez
    global runda
    maciez = {"13": "_", "23": "_", "33": "_", "12": "_", "22": "_", "32": "_", "11": "_", "21": "_", "31": "_"}
    runda = 1
    polegry()
    while True:
        if runda % 2 != 0:
            if player_x == "user":
                user_move("X")
            else:
                ai_move(player_x, "X")
            runda += 1
        else:
            if player_o == "user":
                user_move("O")
            else:
                ai_move(player_o, "O")
            runda += 1

start()
