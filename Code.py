# ATM FACILITATOR SOFTWARE FOR CHILDREN ALONGWITH DIGIT TO WORD CONVERTER
# LOOP-ENABLED VERSION – user can repeat the program until they choose to exit
# Logic preserved exactly, only loop added and structure cleaned

I = 65986  # PRE-CODED AVAILABLE BALANCE

while True:

    print("\n\n         {ATM FACILITATOR SOFTWARE FOR CHILDREN ALONGWITH DIGIT TO WORD CONVERTER}       ")

    c = input("ENTER A FOR WITHDRAWING\nENTER B FOR DEPOSIT\nENTER K FOR CHECKING THE BALANCE\nENTER X TO EXIT\n").upper()

    if c == 'X':
        print("Thank you for using the ATM Facilitator Software!")
        break

    # If the user does not enter A, B, K properly, default to showing balance
    if not c:
        print("No option entered. Showing balance.")
        b = str(I)
    else:
        if c == 'A':
            try:
                r = int(input("AMOUNT TO WITHDRAW\n"))
            except ValueError:
                print("Invalid amount entered. Using existing balance.")
                r = 0

            if r < I:
                a = I - r
                b = str(a)
                I = a     # update the running balance
            else:
                print("insufficient balance")
                b = str(I)

        elif c == 'B':
            try:
                r = int(input("enter the amount\n"))
            except ValueError:
                print("Invalid amount entered. Deposit ignored.")
                r = 0

            a = I + r
            b = str(a)
            I = a        # update the running balance

        elif c == 'K':
            a = I
            b = str(a)

        else:
            print("Invalid option selected. Showing balance.")
            b = str(I)

    # Convert the final numeric string b into a list of digits
    l1 = list(b)
    l = len(l1)

    # Dictionaries
    d = {
        '0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    d1 = {
        '0': '', '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty',
        '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninty'
    }

    d3 = {
        '0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen',
        '5': 'fifteen', '6': 'sixteen', '7': 'seventeen', '8': 'eighteen', '9': 'ninteen'
    }

    z = ""

    # Single digit
    if len(l1) < 2:
        i = l1[0]
        z = d[i]
        print("FINAL AMOUNT IN WORDS", z)

    # two digits starting with 1 (10–19)
    elif len(l1) == 2 and l1[0] == '1':
        z = d3[l1[1]]
        print("FINAL AMOUNT IN WORDS", z)

    # two digits not starting with 1
    elif len(l1) == 2 and l1[0] != '1':
        tens = l1[0]
        ones = l1[1]
        z = d1[tens] + d[ones]
        print("FINAL AMOUNT IN WORDS", z)

    # three digits
    elif len(l1) == 3:
        h = l1[0]
        t = l1[1]
        o = l1[2]
        z = d[h] + " hundred " + d1[t] + d[o]
        print("FINAL AMOUNT IN WORDS", z)

    # four digits
    elif len(l1) == 4:
        p = l1[0]
        i2 = l1[1]
        j = l1[2]
        k = l1[3]
        z = d[p] + " thousand " + d[i2] + " hundred " + d1[j] + " " + d[k]
        print("FINAL AMMOUNT IN WORDS", z)

    # five digits
    elif len(l1) == 5:
        p = l1[0]
        t2 = l1[1]
        m = l1[2]
        k2 = l1[3]
        f = l1[4]

        lword = d[m] + " hundred"

        z = d1[p] + " " + d[t2] + " thousand " + lword + " " + d1[k2] + " " + d[f]
        print("FINAL AMOUNT IN WORDS", z)

    # over 100000
    elif len(l1) >= 6:
        print("CHILDREN ACCOUNT DO NOT ALLOW AMOUNT ABOVE 100000")
        continue

    # Ask user if they want to continue
    ch = input("\nDo you want to use the ATM again? (Y/N): ")
    if ch.upper() != 'Y':
        print("Thank you for using the ATM Facilitator Software!")
        break
