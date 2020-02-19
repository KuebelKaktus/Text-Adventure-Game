from random import randint

def Hilfe():
    print(" ___________________________________________________")
    print("|schaue ---------- Schaue dich im Raum um.          |")
    print("|gehe <Richtung> - Gehe in eine bestimmte Richtung. |")
    print("|furze ----------- Furze in den Raum.               |")
    print("|spiele ---------- Spiele ein Spiel.                |")
    print("|beende ---------- Beendet das Spiel.               |")
    print("|hilfe ----------- Zeige diese Hilfsnachricht an.   |")
    print("|___________________________________________________|")
    print(" ")
    
def Furze():
    print("Du hast gefurzt.")

def Spiele_N():
    print("Hier wird nicht gespielt, sondern gearbeitet!")

def Spiele():
    zufall = randint(1,1000)
    raten = 0
    anzahl = 0

    print("Errate die Zahl zwischen 1 und 1000")
    while anzahl < 15:
        raten = int(input(">>> "))
        anzahl = anzahl + 1
        if raten > zufall:
            print("Die Zahl ist kleiner.")
        elif raten < zufall:
            print("Die Zahl ist größer.")
        elif raten == zufall:
            print("Du hast die Zahl", zufall, "erraten und dafür", anzahl, "Versuche gebraucht. Das Passwort für den Geheimraum ist 'Code'. Finde den Geheimraum mit 'gehe geheim'.")
            break 
    if anzahl == 15:
        print("Du hast verloren und die Zahl", zufall,"nicht erraten.")

def Treppenhaus():
    if userinput == "gehe Westen":
        raum = "Büro"
        print("Du bist jetzt im Büro.")
        return raum
    elif userinput == "schaue":
        print("Du befindest dich im Treppenhaus. Hier gibt es: ")
        print("Tür nach Westen")
    elif userinput == "hilfe":
        Hilfe()
    elif userinput == "furze":
        Furze()
    elif userinput == "spiele":
        print("Im Treppenhaus spielt man nicht.")
    else:
        print("Dies war eine falsche Eingabe.")
    return "Treppenhaus"
    

def Büro():
    if userinput == "gehe Osten":
        raum = "Treppenhaus"
        print("Du bist jetzt im Treppenhaus.")
        return raum
    elif userinput == "gehe Süden":
        raum = "Videokonferenzraum"
        print("Du bist jetzt in einem Videokonferenzraum.")
        return raum
    elif userinput == "gehe Westen":
        raum = "Serverraum"
        print ("Du bist jetzt im Serverraum.")
        return raum
    elif userinput == "schaue":
        print("Du befindest dich im Büro. Hier gibt es: ")
        print("Tür nach Osten")
        print("Tür nach Süden")
        print("Tür nach Westen")
        print("Benni")
        print("Ralph")
    elif userinput == "hilfe":
        Hilfe()
    elif userinput == "furze":
        print("Benni: Du hast gefurzt! RAUS!")
        raum = "Treppenhaus"
        print("Du bist jetzt im Treppenhaus.")
        return raum
    elif userinput == "spiele":
        Spiele_N()
    else:
        print("Dies war eine falsche Eingabe.")
    return "Büro"

def Videokonferenzraum():
    if userinput == "gehe Norden":
        raum = "Büro"
        print("Du bist jetzt im Büro")
        return raum
    elif userinput == "gehe geheim":
        eingabe = str(input("Was ist das Passwort? "))
        if eingabe == "Code":
            raum = "Geheimraum"
            print("Das Passwort ist richtig!")
            print("Du bist jetzt im Geheimraum.")
            print("Du findest eine Gehaltserhöhung")
            return raum
        else:
            print("Das Passwort ist falsch.")
    elif userinput == "schaue":
        print("Du befindest dich in einem Videokonferenzraum. Hier gibt es: ")
        print("Tür nach Norden")
        print("Miriam")
    elif userinput == "hilfe":
        Hilfe()
    elif userinput == "furze":
        Furze()
    elif userinput == "spiele":
        Spiele_N()
    else:
        print("Dies war eine falsche Eingabe.")
    return "Videokonferenzraum"

def Serverraum():
    if userinput == "gehe Osten":
        raum = "Büro"
        print("Du bist jetzt im Büro")
        return raum
    elif userinput == "gehe Westen":
        raum = "Pausenraum"
        print("Du bist jetzt im Pausenraum")
        return raum
    elif userinput == "schaue":
        print("Du befindest dich im Serverraum. Hier gibt es: ")
        print("Tür nach Osten")
        print("Tür nach Westen")
    elif userinput == "hilfe":
        Hilfe()
    elif userinput == "furze":
        Furze()
    elif userinput == "spiele":
        Spiele_N()
    else:
        print("Dies war eine falsche Eingabe.")
    return "Serverraum"

def Pausenraum():
    if userinput == "gehe Osten":
        raum = "Serverraum"
        print("Du bist jetzt im Serverraum.")
        return raum
    elif userinput == "spiele":
        Spiele()
    elif userinput == "schaue":
        print("Du befindest dich im Pausenraum. Hier gibt es: ")
        print("Tür nach Osten")
        print("Spiel")
    elif userinput == "hilfe":
        Hilfe()
    elif userinput == "furze":
        Furze()
    else:
        print("Dies war eine falsche Eingabe.")
    return "Pausenraum"

def Geheimraum():
    if userinput == "gehe Norden":
        raum = "Videokonferenzraum"
        print("Du bist jetzt in einem Videokonferenzraum.")
        return raum
    elif userinput == "schaue":
        print("Du befindest dich im Geheimraum. Hier gibt es: ")
        print("Tür nach Norden")
        print("Gehaltserhöhung")
    elif userinput == "hilfe":
        Hilfe()
    elif userinput == "furze":
        Furze()
    elif userinput == "spiele":
        Spiele_N()
    else:
        print("Dies war eine falsche Eingabe.")
    return "Geheimraum"


raum = "Treppenhaus"

print("Willkommen in meinem Spiel")

print('mit "hilfe" kannst du dir alle Befehle anschauen')

print("Du bist im " + raum)
userinput = str(input(">>> "))

while userinput != "beende":
    
    if raum == "Treppenhaus":
        raum = Treppenhaus()
        
    elif raum == "Büro":
        raum = Büro()
    
    elif raum == "Videokonferenzraum":
        raum = Videokonferenzraum()
        
    elif raum == "Serverraum":
        raum = Serverraum()
        
    elif raum == "Pausenraum":
        raum = Pausenraum()
        
    elif raum == "Geheimraum":
        raum = Geheimraum()
    
    userinput = input(">>> ")
    
print("Das Spiel ist vorbei!")