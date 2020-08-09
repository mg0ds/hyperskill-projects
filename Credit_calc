import math
import sys
import getopt

full_args = sys.argv
arg_list = full_args[1:]
short_options = ["t:pr:pay:per:i:"]
long_options = ["type=", "principal=", "payment=", "periods=", "interest="]
aaa = []
try:
    arguments, values = getopt.getopt(arg_list, short_options, long_options)

    type = ""
    principal = 0
    payment = 0
    periods = 0
    interest = 0

    for current_argument, current_value in arguments: #przypisanie argumentow
        if "--type" == current_argument:
            type = current_value
        elif "--principal" == current_argument:
            principal = int(current_value)
        elif "--payment" == current_argument:
            payment = int(current_value)
        elif "--periods" == current_argument:
            periods = int(current_value)
        elif "--interest" == current_argument:
            interest = float(current_value)

    if len(arg_list) < 4 or type == "" or (type == "diff" and payment != 0) or interest == 0 or (principal < 0 or payment < 0 or periods < 0 or interest < 0):
        print("Incorrect parameters")
    else:
        if type == "diff" and principal != 0 and periods != 0 and interest != 0:
            wplacone_pieniondze = 0
            for m in range(1, periods + 1):
                i = interest / 1200.0
                D = (principal / periods) + i * (principal - ((principal * (m - 1)) / periods))
                wplacone_pieniondze += math.ceil(D)
                print("Month {}: paid out {}".format(m, math.ceil(D)))
            overpayment = wplacone_pieniondze - principal
            print("\nOverpayment = {}".format(overpayment))
        elif type == "annuity" and principal != 0 and periods != 0 and interest != 0:
            i = interest / 1200.0
            a = principal * ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))
            print("Your annuity payment = {}!".format(math.ceil(a)))
            overpayment = (math.ceil(a) * periods) - principal
            print("Overpayment = {}".format(overpayment))
        elif type == "annuity" and payment != 0 and periods != 0 and interest != 0:
            i = interest / 1200.0
            p = payment / ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))
            print("Your credit principal = {}!".format(math.floor(p)))
            overpayment = (payment * periods) - math.floor(p)
            print("Overpayment = {}".format(overpayment))
        elif type == "annuity" and principal != 0 and payment != 0 and interest != 0:
            i = interest / 1200.0
            n = math.log((payment / (payment - (i * principal))), 1 + i)
            if math.ceil(n) == 12:
                print("You need 1 year to repay this credit!")
            elif math.ceil(n) % 12 == 0:
                ilosc_lat = int(math.ceil(n) / 12)
                print("You need {} years to repay this credit!".format(ilosc_lat))
            elif math.ceil(n) < 12:
                print("You need {} months to repay this credit!".format(math.ceil(n)))
            else:
                lata = int(math.ceil(n) / 12)
                mies = math.ceil(n) - lata * 12
                print("You need {} years and {} months to repay this credit!".format(lata, mies))
            overpayment = (payment * math.ceil(n)) - principal
            print("Overpayment = {}".format(overpayment))
except getopt.error as err:
    print("Incorrect parameters")
