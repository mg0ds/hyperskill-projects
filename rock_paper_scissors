import random

name = input("Enter your name: ")
print("Hello, " + name)
score = 0
"""
plik = open("rating.txt", "r")

for i in plik:
    na, sc = i.split()
    if na == name:
        score = int(sc)
"""

gra = input("Input new list or leave blank for classic game")
if gra == "":
    aaa = ["rock", "paper", "scissors"]
else:
    aaa = gra.split(",")


while True:
    print("cala lista: " + str(aaa))

    co = input()
    if co == "!exit" or co =="!rating" or co in aaa:
        if co == "!exit":
            print("Bye!")
            break
        elif co =="!rating":
            print("Your rating: " + str(score))
        else:
            bbb = random.choice(aaa)
            print("comp wybral: " + bbb)
            wygrywaja = []
            przegryw = []
            if bbb == co:
                print("There is a draw ({})".format(bbb))
                score += 50
            else:
                dlugosc_listy = (len(aaa) - 1) / 2
                if aaa.index(co) > dlugosc_listy:
                    przegryw = aaa[aaa.index(co) + 1:]
                    wygrywaja = aaa[:aaa.index(co)]
                    przejscie_listy = aaa.index(co) + dlugosc_listy - len(aaa) + 1
                    przegryw = przegryw + aaa[0:int(przejscie_listy)]
                    del wygrywaja[0:int(przejscie_listy)]
                elif aaa.index(co) < dlugosc_listy:
                    przegryw = aaa[aaa.index(co) + 1:aaa.index(co) + int(dlugosc_listy) + 1]
                    wygrywaja = aaa.copy()
                    del wygrywaja[aaa.index(co):aaa.index(co) + int(dlugosc_listy) + 1]
                else:
                    przegryw = aaa[aaa.index(co) + 1:]
                    wygrywaja = aaa[:aaa.index(co)]
                print(wygrywaja)
                print(przegryw)
                if bbb in wygrywaja:
                    print("Well done. Computer chose {} and failed".format(bbb))
                    score += 100
                elif bbb in przegryw:
                    print("Sorry, but computer chose {}".format(bbb))
    else:
        print("Invalid input")
