
raum = "Treppenhaus"

print("Willkommen in meinem Spiel")

print('mit "hilfe" kannst du dir alle Befehle anschauen')

print("Du bist im " + raum)
userinput = str(input(">>> "))

while userinput != "beende":
    if raum == "Treppenhaus" and userinput == "gehe Westen":
        raum = "Büro"
        print("Du bist jetzt im Büro.")
        
    elif raum == "Treppenhaus" and userinput == "schaue":
        print("Du befindest dich im Treppenhaus. Hier gibt es: ")
        print("Tür nach Westen")
        
    elif raum == "Büro" and userinput == "gehe Osten":
        raum = "Treppenhaus"
        print("Du bist jetzt im Treppenhaus.")
        
    elif raum == "Büro" and userinput == "schaue":
        print("Du befindest dich im Büro. Hier gibt es: ")
        print("Tür nach Osten")
        print("Benni")
        print("Ralph")
    
    elif userinput == "hilfe":
        print(" __________________________________________________")
        print("|schaue------------Schaue dich im Raum um.         |")
        print("|gehe <Richtung>---Gehe in eine bestimmte Richtung |")
        print("|beende------------beendet das Spiel               |")
        print("|hilfe-------------Zeige diese Hilfsnachricht an   |")
        print("|__________________________________________________|")
    else:
        print("Dies war eine falsche Eingabe.")
    userinput = input(">>> ")

print("Das Spiel ist vorbei!")