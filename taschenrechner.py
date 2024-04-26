from time import sleep
def calc():
    print("==============================================")
    print("Taschenrechner")
    print("Made by Fatmira")

    print("Benutzbare Rechenarten: + | - | / | * |")
    user = input("Auswahl: ")
    print("")

    match user:
        case"+":
            print("Ausgewählt: +")
            print("")
            ZahlAdd = float(input("Zahl 1: "))
            ZahlAdd2 = float(input("Zahl 2: "))
            print("")
            ergebnisAdd = (ZahlAdd + ZahlAdd2)
            print("Das Ergebnis: " , ergebnisAdd)
            print("Rechnung: ", ZahlAdd ," + ", ZahlAdd2)
            print("==============================================")
            sleep(3)
            return calc()

        case"-":
            print("Ausgewählt: -")
            print("")
            ZahlSub = float(input("Zahl 1: "))
            ZahlSub2 = float(input("Zahl 2: "))
            print("")
            ergebnisSub = (ZahlSub - ZahlSub2)
            print("Das Ergebnis: ", ergebnisSub)
            print("Rechnung: ", ZahlSub, " - ", ZahlSub2)
            print("==============================================")
            sleep(3)
            return calc()

        case"/":
            print("Ausgewählt: /")
            print("")
            ZahlDiv = float(input("Zahl 1: "))
            ZahlDiv2 = float(input("Zahl 2: "))
            print("")
            ergebnisDiv = (ZahlDiv / ZahlDiv2)
            print("Das Ergebnis: ", "%.2f" % ergebnisDiv)
            print("Rechnung: ", ZahlDiv, " / ", ZahlDiv2)
            print("==============================================")
            sleep(3)
            return calc()

        case"*":
            print("Ausgewählt: *")
            print("")
            ZahlMul = float(input("Zahl 1: "))
            ZahlMul2 = float(input("Zahl 2: "))
            print("")
            ergebnisMul = (ZahlMul * ZahlMul2)
            print("Das Ergebnis: ", ergebnisMul)
            print("Rechnung: ", ZahlMul, " * ", ZahlMul2)
            print("==============================================")
            sleep(3)
            return calc()

        case _:
            print("Ungültig.")
            print("")
            return calc()
calc()
