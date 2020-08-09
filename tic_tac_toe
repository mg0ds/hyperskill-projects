def polegry():
    print("---------")
    print("| {} {} {} |".format(maciez["13"], maciez["23"], maciez["33"]))
    print("| {} {} {} |".format(maciez["12"], maciez["22"], maciez["32"]))
    print("| {} {} {} |".format(maciez["11"], maciez["21"], maciez["31"]))
    print("---------\n")

def spr():
    wygrana = [[maciez["13"], maciez["12"], maciez["11"]], [maciez["23"], maciez["22"], maciez["21"]], [maciez["33"],
                maciez["32"], maciez["31"]], [maciez["13"], maciez["23"], maciez["33"]], [maciez["12"], maciez["22"],
                maciez["32"]], [maciez["11"], maciez["21"], maciez["31"]], [maciez["13"], maciez["22"], maciez["31"]],
               [maciez["33"], maciez["22"], maciez["11"]]]
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
    if xwin == 1:
        print("X wins")
        return "koniec"
    elif owin == 1:
        print("O wins")
        return "koniec"
    elif runda == 10 and xwin == 0 and owin == 0:
        print("Draw")
        return "koniec"

maciez = {"13": "_", "23": "_", "33": "_", "12": "_", "22": "_", "32": "_", "11": "_", "21": "_", "31": "_"}
runda = 1
polegry()

while True:
    rxry = input("Enter the coordinates:").replace(" ", "")
    if rxry.isdigit():
        if int(rxry[0]) in range(1, 4) and int(rxry[1]) in range(1, 4) and len(rxry) == 2:
            if maciez[rxry] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                if runda % 2 != 0:
                    maciez[rxry] = "X"
                else:
                    maciez[rxry] = "O"
                runda += 1
                polegry()
                if spr() == "koniec":
                    break
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
