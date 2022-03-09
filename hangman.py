import random

lista = ["python", "java", "kotlin", "javascript"]
print("H A N G M A N")

while True:
    menu = input("Type 'play' to play the game, 'exit' to quit:")
    if menu == "play":
        a = random.choice(lista)
        b = list(a)
        aukryte = list("-" * len(a))
        zycie = 0
        poprzednia_litera = set()
        zgadles = set()
        while zycie < 8:
            print("\n")
            print("".join(aukryte))
            litera = input("Input a letter:")
            if len(litera) == 1:
                if litera.isascii() == True and litera.islower() == True:
                    if litera not in poprzednia_litera:
                        if litera in set(a) and litera not in zgadles:
                            for aaa in range(1, a.count(litera) + 1):
                                pozycja = b.index(litera)
                                aukryte[pozycja] = litera
                                b[pozycja] = "-"
                                zgadles.add(litera)
                            if aukryte == list(a):
                                print("You guessed the word!\nYou survived!")
                                break
                        elif litera not in set(a):
                            print("No such letter in the word")
                            zycie += 1
                    else:
                        print("You already typed this letter")
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                print("You should input a single letter")
            poprzednia_litera.add(litera)
        if zycie == 8:
            print("You are hanged!")
    elif menu == "exit":
        break
