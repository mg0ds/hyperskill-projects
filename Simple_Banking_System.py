import random
import sqlite3
conn = sqlite3.connect("card.s3db")


def menu():
    print("1. Create an account\n2. Log into account\n0. Exit")
    menu_wybor = int(input())
    print("")
    if menu_wybor == 1:
        create_account()
    elif menu_wybor == 2:
        login()
    elif menu_wybor == 0:
        print("Bye!\n")
        cur.close()


def luhn(luhn_check_number):
    if len(luhn_check_number) == 15:
        i = 1
        luhn_check = 0
        sixteen = 0
        for digit in luhn_check_number:
            if i % 2 != 0:
                a = int(digit) * 2
                if a > 9:
                    luhn_check += (a - 9)
                else:
                    luhn_check += a
            else:
                luhn_check += int(digit)
            i += 1
        if luhn_check % 10 != 0:
            sixteen = 10 - int(str(luhn_check)[-1])
        return sixteen
    elif len(luhn_check_number) == 16:
        fifteen = luhn_check_number[0:15]
        sixteen_digit = luhn_check_number[15]
        i = 1
        luhn_check = 0
        sixteen_check = 0
        for digit in fifteen:
            if i % 2 != 0:
                a = int(digit) * 2
                if a > 9:
                    luhn_check += (a - 9)
                else:
                    luhn_check += a
            else:
                luhn_check += int(digit)
            i += 1
        if luhn_check % 10 != 0:
            sixteen_check = 10 - int(str(luhn_check)[-1])
        if int(sixteen_digit) == sixteen_check:
            return 1
        else:
            return -1


def create_account():
    print("Your card has been created\nYour card number:")
    new_customer_account_number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    new_customer_account_number = ""
    for i in range(0, 9):
        new_customer_account_number_list[i] = random.randrange(0, 9)
        new_customer_account_number += str(new_customer_account_number_list[i])
    new_card_number = "400000" + str(new_customer_account_number)
    new_card_number += str(luhn(new_card_number))
    print(new_card_number)
    print("Your card PIN:")
    new_PINlist = [0, 0, 0, 0]
    new_PIN = ""
    for i in range(0, 4):
        new_PINlist[i] = random.randrange(0, 9)
        new_PIN += str(new_PINlist[i])
    print(new_PIN + "\n")
    cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (new_card_number, new_PIN))
    conn.commit()
    cur.execute('SELECT * FROM card')
    menu()


def login():
    login_customer_account_number = input("Enter your card number:\n")
    cur.execute('SELECT number, pin FROM card WHERE number = ?', (login_customer_account_number,))
    account_fromdb = cur.fetchone()
    login_pin = input("Enter your PIN:\n")
    if account_fromdb == None or (account_fromdb[0] == "" or account_fromdb[1] != login_pin):
        print("\nWrong card number or PIN!\n")
        menu()
    else:
        print("\nYou have successfully logged in!\n")
        loginOK(login_customer_account_number)


def loginOK(login_customer_account_number):
    login_menu = int(input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n"""))
    print("")

    if login_menu == 1:
        cur.execute('SELECT balance FROM card WHERE number = ?', (login_customer_account_number,))
        balance_fromdb = cur.fetchone()
        print("Balance: " + str(balance_fromdb[0]) + "\n")
        loginOK(login_customer_account_number)
    elif login_menu == 2:
        add_income = input("Enter income: \n")
        cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (add_income, login_customer_account_number))
        conn.commit()
        print("Income was added!\n")
        loginOK(login_customer_account_number)
    elif login_menu == 3:
        transfer_to_number = input("Transfer\nEnter card number:\n")
        if transfer_to_number == login_customer_account_number:
            print("You can't transfer money to the same account!\n")
            loginOK(login_customer_account_number)
        cur.execute('SELECT * FROM card WHERE number = ?', (transfer_to_number,))
        is_number_ok = cur.fetchone()
        if is_number_ok != None: #card number in db
            how_much_to_transfer = input("Enter how much money you want to transfer:\n")
            cur.execute('SELECT balance FROM card WHERE number = ?', (login_customer_account_number,))
            balance_fromdb = cur.fetchone()
            if int(balance_fromdb[0]) < int(how_much_to_transfer):
                print("Not enough money!\n")
                loginOK(login_customer_account_number)
            else:
                cur.execute("UPDATE card SET balance = balance - ? WHERE number = ?",
                            (how_much_to_transfer, login_customer_account_number))
                conn.commit()
                cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?",
                            (how_much_to_transfer, transfer_to_number))
                conn.commit()
                print("Success!\n")
                loginOK(login_customer_account_number)
        else:
            if luhn(transfer_to_number) == 1:
                print("Such a card does not exist.\n")
                loginOK(login_customer_account_number)
            else:
                print("Probably you made mistake in the card number. Please try again!\n")
                loginOK(login_customer_account_number)
    elif login_menu == 4:
        cur.execute("DELETE FROM card WHERE number = ?", (login_customer_account_number,))
        conn.commit()
        print("The account has been closed!")
        menu()
    elif login_menu == 5:
        print("You have successfully logged out!\n")
        menu()
    elif login_menu == 0:
        print("Bye!\n")
        cur.close()


cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    number TEXT UNIQUE NOT NULL, 
    pin TEXT NOT NULL, 
    balance INTEGER DEFAULT 0
    );''')

menu()
